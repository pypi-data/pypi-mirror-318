# LightAgent

**LightAgent** 是一个极其轻量的带记忆（`mem0`）、工具（`Tools`）、思维树（`ToT`）的主动式 Agent 框架。它支持类 Swarm 的多智能体协同、自动化工具生成、Agent 测评，底层模型支持 OpenAI、智谱 ChatGLM、百川大模型、DeepSeek、Qwen 系列大模型等。同时，LightAgent 支持 OpenAI 流格式 API 服务输出，无缝接入各大主流 Chat 框架。

---

## 特性

- **轻量高效**：极简设计，快速部署，适合各种规模的应用场景。
- **记忆支持**：内置 `mem0` 记忆模块，支持上下文记忆和历史记录管理。
- **工具集成**：支持自定义工具（`Tools`），自动化工具生成，灵活扩展。
- **思维树（ToT）**：内置思维树模块，支持复杂任务分解和多步推理。
- **多智能体协同**：支持类 Swarm 的多智能体协同工作，提升任务处理效率。
- **多模型支持**：兼容 OpenAI、智谱 ChatGLM、百川大模型、DeepSeek、Qwen 系列大模型。
- **流式 API**：支持 OpenAI 流格式 API 服务输出，无缝接入主流 Chat 框架。
- **Agent 测评**：内置 Agent 测评工具，方便评估和优化 Agent 性能。

---

## 快速开始

### 安装

```bash
pip install lightagent
```

### 示例代码

```python
from lightagent import LightAgent

# 初始化 Agent
agent = LightAgent(model="openai", api_key="your_api_key")

# 定义工具
def search_news(query: str, top_k: int) -> str:
    """
    实时检索互联网上的信息
    :param query: 检索信息
    :param top_k: 返回条数
    :return: 检索结果
    """
    return f"检索结果: {query}, top_k: {top_k}"

# 注册工具
agent.register_tool(search_news)

# 运行 Agent
response = agent.run("请搜索最近关于大模型技术的新闻", tools=["search_news"])
print(response)
```

---

## 功能详解

### 1. 记忆模块（`mem0`）
LightAgent 内置 `mem0` 记忆模块，支持上下文记忆和历史记录管理。通过记忆模块，Agent 可以在多轮对话中保持上下文一致性。

```python
# 启用记忆模块
agent.enable_memory()
```

### 2. 工具集成
支持自定义工具（`Tools`），并通过 `register_tool` 方法注册工具。工具可以是任意 Python 函数，支持参数类型注解和自动生成工具描述。

```python
# 定义工具
def get_weather(city: str) -> str:
    """
    获取城市天气信息
    :param city: 城市名称
    :return: 天气信息
    """
    return f"城市 {city} 的天气信息"

# 注册工具
agent.register_tool(get_weather)
```

### 3. 思维树（ToT）
内置思维树模块，支持复杂任务分解和多步推理。通过思维树，Agent 可以更好地处理复杂任务。

```python
# 启用思维树
agent.enable_tot()
```

### 4. 多智能体协同
支持类 Swarm 的多智能体协同工作，提升任务处理效率。多个 Agent 可以协同完成复杂任务。

```python
# 创建多个 Agent
agent1 = LightAgent(model="chatglm")
agent2 = LightAgent(model="openai")

# 协同工作
response = agent1.collaborate(agent2, "请分析最近的市场趋势")
```

### 5. 多模型支持
兼容多种大模型，包括 OpenAI、智谱 ChatGLM、百川大模型、DeepSeek、Qwen 系列大模型。

```python
# 使用智谱 ChatGLM 模型
agent = LightAgent(model="chatglm")
```

### 6. 流式 API
支持 OpenAI 流格式 API 服务输出，无缝接入主流 Chat 框架。

```python
# 启用流式输出
response = agent.run("请生成一篇关于 AI 的文章", stream=True)
for chunk in response:
    print(chunk)
```

### 7. Agent 测评
内置 Agent 测评工具，方便评估和优化 Agent 性能。

```python
# 运行测评
evaluation_result = agent.evaluate("请回答以下问题：什么是大模型？")
print(evaluation_result)
```

---

## 使用场景

- **智能客服**：通过多轮对话和工具集成，提供高效的客户支持。
- **数据分析**：利用思维树和多智能体协同，处理复杂的数据分析任务。
- **自动化工具**：通过自动化工具生成，快速构建定制化工具。
- **教育辅助**：通过记忆模块和流式 API，提供个性化的学习体验。

---

## 贡献指南

我们欢迎任何形式的贡献！如果您有好的想法或发现 Bug，请提交 Issue 或 Pull Request。

1. Fork 本项目。
2. 创建您的分支：`git checkout -b feature/YourFeature`。
3. 提交您的更改：`git commit -m 'Add some feature'`。
4. 推送分支：`git push origin feature/YourFeature`。
5. 提交 Pull Request。

---

## 许可证

LightAgent 采用 [Apache 许可证](LICENSE)。

---

## 联系我们

如有任何问题或建议，请联系我们：

- 邮箱：156713035@qq.com
- GitHub Issues: [https://github.com/wxai-space/lightagent/issues](https://github.com/wxai-space/lightagent/issues)

---

**LightAgent** —— 轻量、灵活、强大的主动式 Agent 框架，助您快速构建智能应用！