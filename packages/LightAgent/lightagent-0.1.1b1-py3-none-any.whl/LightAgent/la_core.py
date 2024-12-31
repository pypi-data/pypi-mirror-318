import json
import time

from loguru import logger
import inspect
import traceback
import requests
from typing import Callable, Any, Dict
import json
from datetime import datetime
from openai import OpenAI
from colorama import init, Fore

# Global registry for tools
from typing import List, Dict, Any, Callable
from copy import deepcopy

# 全局工具注册表
_FUNCTION_MAPPINGS = {}  # 工具名称 -> 工具函数
_OPENAI_FUNCTION_SCHEMAS = []  # OpenAI 格式的工具描述

def register_tool_manually(tools: List[Callable]) -> None:
    """
    手动注册多个工具，从函数属性中提取工具信息
    :param tools: 工具函数列表
    """
    for func in tools:
        if not hasattr(func, "tool_info"):
            raise ValueError(f"Function `{func.__name__}` does not have tool_info attribute.")

        tool_info = func.tool_info
        tool_name = tool_info["tool_name"]
        _FUNCTION_MAPPINGS[tool_name] = func  # 注册工具

        # 构建 OpenAI 格式的工具描述
        tool_params_openai = {}
        tool_required = []
        for param in tool_info["tool_params"]:
            tool_params_openai[param["name"]] = {
                "type": param["type"],
                "description": param["description"],
            }
            if param["required"]:
                tool_required.append(param["name"])

        tool_def_openai = {
            "type": "function",
            "function": {
                "name": tool_name,
                "description": tool_info["tool_description"],
                "parameters": {
                    "type": "object",
                    "properties": tool_params_openai,
                    "required": tool_required,
                },
            }
        }

        _OPENAI_FUNCTION_SCHEMAS.append(tool_def_openai)

def dispatch_tool(tool_name: str, tool_params: Dict[str, Any]) -> str:
    """
    调用工具
    """
    if tool_name not in _FUNCTION_MAPPINGS:
        return f"Tool `{tool_name}` not found."

    tool_call = _FUNCTION_MAPPINGS[tool_name]
    try:
        print(f"Calling tool: {tool_name} with params: {tool_params}")  # 调试信息
        return str(tool_call(**tool_params))
    except Exception as e:
        print(f"Tool call failed: {e}")  # 调试信息
        return traceback.format_exc()

def get_tools() -> List[Dict[str, Any]]:
    """
    获取所有工具的描述（OpenAI 格式）
    """
    return deepcopy(_OPENAI_FUNCTION_SCHEMAS)
    
class MultiAgentSystem:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __call__(self, *args, **kwargs):
        raise NotImplementedError("MultiAgentSystem must implement the __call__ method.")


class Tool:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Tool must implement the __call__ method.")

class LightAgent:
    def __init__(self, model: str, api_key: str, base_url: str , memory: bool = False, chain_of_thought: bool = False):
        self.model = model
        self.base_url = base_url
        self.api_key = api_key
        self.client = OpenAI(
            base_url = self.base_url,
            api_key = self.api_key
        )

    def run(self, query: str, stream=False, tools=[], max_retry=5):
        # logger.info(f"\n开始思考问题: {query}")
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")
        SYSTEM_PROMPT = f"请记住你是万行一言AI金融搜索，请帮用户完成的金融数据查询和信息检索。请一步一步思考来完成用户的要求。尽可能拆解用户的输入先检索再回答。 /n 今日的日期: {current_date} 当前时间: {current_time}"

        params = dict(model=self.model, messages=[{"role": "system", "content": SYSTEM_PROMPT},{"role": "user", "content": query}], stream=stream)
        if tools:
            register_tool_manually(tools)
            print("Registered tools:", _FUNCTION_MAPPINGS.keys())

            tools = get_tools()
            params["tools"] = tools
        response = self.client.chat.completions.create(**params)
        # print(response)

        for _ in range(max_retry):
            if not stream:
                if response.choices[0].message.tool_calls:
                    function_call = response.choices[0].message.tool_calls[0].function
                    # print(function_call,type)
                    print(f"Function Call Response: {function_call.model_dump()}")

                    function_args = json.loads(function_call.arguments)
                    tool_response = dispatch_tool(function_call.name, function_args)
                    logger.info(f"Tool Call Response: {tool_response}")

                    # params["messages"].append(response.choices[0].message)
                    params["messages"].append(
                        {
                            "role": "assistant",
                            "content": json.dumps(function_call.model_dump()),  # 调用ai接口返回的文本
                        }
                    )
                    params["messages"].append(
                        {
                            "role": "user",
                            "name": function_call.name,
                            "content": tool_response,  # 调用函数返回结果
                        }
                    )
                else:
                    reply = response.choices[0].message.content
                    # logger.info(f"Final Reply: \n{reply}")
                    return reply

            else:
                output = ""
                function_call = []
                function_call_name = ""
                function_call_arguments = ""
                for chunk in response:

                    content = chunk.choices[0].delta.content or ""
                    print(Fore.BLUE + content, end="", flush=True)
                    output += content

                    try:
                        if chunk.choices and chunk.choices[0].delta.tool_calls:
                            argumentsTxt = chunk.choices[0].delta.tool_calls[0].function.arguments
                            # 检查 argumentsTxt 是否为空
                            if argumentsTxt:
                                function_call_arguments += argumentsTxt
                    except (IndexError, AttributeError, KeyError):
                        pass

                    try:
                        if function_call_name == '' and chunk.choices[0].delta.tool_calls:
                            function_call_name=chunk.choices[0].delta.tool_calls[0].function.name
                    except (IndexError, AttributeError, KeyError):
                        pass

                    if chunk.choices[0].finish_reason == "stop":
                        return output

                    elif chunk.choices[0].finish_reason == "tool_calls":
                        function_call={
                            "name":function_call_name,
                            "arguments":function_call_arguments,
                        }
                        # function_call = json.dumps(function_call_dist,ensure_ascii=False)
                        # print(function_call)

                        logger.info(f"正在调用工具: {function_call}")

                        function_args = json.loads(function_call["arguments"])
                        tool_response = dispatch_tool(function_call["name"], function_args)
                        # logger.info(f"工具响应: {tool_response}")

                        params["messages"].append(
                            {
                                "role": "assistant",
                                "content": output,  # 调用ai接口返回的文本
                            }
                        )
                        params["messages"].append(
                            {
                                "role": "function",
                                "name": function_call["name"],
                                "content": tool_response,
                            }
                        )

                        break

            # print(params)
            response = self.client.chat.completions.create(**params)
            # return response

        return "Failed to generate a valid response."


if __name__ == "__main__":
    # Example of registering and using a tool
    print("This is LightAgent")
    # print(dispatch_tool("example_tool", {"param1": "test"}))
