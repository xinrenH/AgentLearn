# 阶段2：第一个 Agent（Tool Calling）— 学习任务说明文档

> **定位**：给 LLM "配工具"——让它不仅能说话，还能做事。这是从"聊天机器人"到"智能体"的质变。
> **前置条件**：完成阶段 1（LLM API 调用），能稳定调 LLM、处理结构化输出。
> **总时长**：每天 2 小时，约 1-2 周完成。

---

## 学习前必读：Tool Calling 到底是什么？

**核心原理（一句话）**：LLM 不"执行"工具，它只"建议"调用哪个工具、传什么参数。你的 Python 代码才是真正执行工具的人。

**完整流程**：
```
用户: "北京今天天气怎么样？"
  ↓
LLM 分析 → 需要调用 get_weather 工具，参数 city="北京"
  ↓
你的代码: 执行 get_weather("北京") → 拿到结果 "北京今天 25°C，晴"
  ↓
把结果发回 LLM
  ↓
LLM: "北京今天天气晴朗，气温 25°C，适合出行。"
```

**关键认知**：你和 LLM 之间是一个"协作循环"——LLM 提出要调什么工具，你执行后把结果喂回去，LLM 再基于结果生成最终回答。

---

## 学习任务 1：用 PydanticAI 跑通第一个 Agent

### 任务目标
用代码最少的框架（PydanticAI）跑通"Agent = LLM + 工具"。

### 为什么选 PydanticAI？
- 代码最少，概念最简单（Agent + Tool + RunContext 三个概念就够）
- 类型安全，工具函数的入参出参全是 Pydantic 校验过的
- 官方文档质量极高，有完整的 example 项目

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 1.1 | 安装 PydanticAI | `pip install pydantic-ai`，配置好 API Key |
| 1.2 | Hello World Agent | 5 行代码跑通：创建 Agent → 调用 `run_sync()` → 打印结果 |
| 1.3 | 第一个工具 | 用 `@agent.tool` 注册 `get_current_time()`，返回当前时间字符串。Agent 自动判断何时调用它 |
| 1.4 | 观察工具调用 | 打印 Agent 运行过程中的 messages 列表，观察 LLM 发出的 `tool_calls` 和你的工具返回的 `tool` 消息 |

### 产出物
- `hello_agent.py` — 第一个可运行的 Agent
- 理解 `RunContext` 的作用：在工具函数间传递共享状态

### 验收标准
- Agent 能根据用户问题自动决定是否调用工具
- 能观察到完整的 tool calling 消息流转

---

## 学习任务 2：多工具 Agent

### 任务目标
给 Agent 配多个工具，Agent 能根据用户意图自动选择正确的工具。

### 学习内容
- 工具描述（docstring）的重要性：LLM 读你的 docstring 来决定该不该调这个工具
- 工具参数的类型注解：LLM 根据类型来填参数
- 多个工具时如何避免 LLM 选错

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 2.1 | 创建 3 个工具 | (1) `get_weather(city: str) -> str` (2) `calculate(expression: str) -> float` (3) `search_web(query: str) -> str`（用 `duckduckgo_search` 库） |
| 2.2 | 注册并测试 | 把所有工具注册给同一个 Agent。依次测试："北京天气？""12345×6789？""最近的 AI 新闻？"——Agent 必须选对工具 |
| 2.3 | 多工具组合 | 问一个需要多个工具的问题："北京天气多少度？把温度从摄氏度转成华氏度"——Agent 要先调 `get_weather` 再调 `calculate` |
| 2.4 | 工具描述优化 | 故意写一个模糊的 docstring（如"获取信息"），观察 LLM 会不会选错。然后改写成精确描述（如"查询指定城市的当前天气和温度"），对比效果 |

### 产出物
- `multi_tool_agent.py` — 含 3 个真实工具的多工具 Agent
- 一份对比记录：docstring 质量对工具选择准确率的影响

### 验收标准
- Agent 在 3 个工具中自动选对正确的工具
- Agent 能连续调用多个工具解决复合问题
- 理解工具 docstring 写得好不好直接影响 Agent 表现

---

## 学习任务 3：工具调用的健壮性

### 任务目标
处理工具调用的各种异常情况——LLM 传错参数、工具执行失败、超时等。

### 学习内容
- LLM 可能传错参数类型（字符串当数字）
- 工具函数内部可能出错（网络中断、数据库崩了）
- 错误信息如何优雅地返回给 LLM 让它重试
- 工具调用超时控制

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 3.1 | 参数容错 | 写 `get_weather(city: str)`，但 LLM 可能传 `city=123`。在工具内部做类型检查，返回友好错误信息 |
| 3.2 | 工具故障模拟 | 给工具加 30% 的随机失败概率，失败时返回 `{"error": "服务暂时不可用，请稍后重试"}`。观察 LLM 收到错误后如何处理 |
| 3.3 | 重试机制 | 工具失败后，Agent 自动重试（让 LLM 重新决定是否再调一次）最多 3 次 |
| 3.4 | 降级策略 | 3 次重试都失败后，Agent 向用户解释"当前无法获取该信息"，并尝试用其他知识回答 |

### 产出物
- `robust_agent.py` — 有容错、重试、降级的健壮 Agent
- 记录常见的工具调用失败模式

### 验收标准
- 工具失败不会导致程序崩溃
- LLM 收到错误信息后能做出合理反应
- 有完整的重试 + 降级逻辑

---

## 学习任务 4：理解 Tool Calling 底层机制

### 任务目标
不看框架封装，直接看 OpenAI API 原始交互，理解 Function Calling 的底层协议。

### 学习内容
- OpenAI API 的 `tools` 参数格式（JSON Schema 描述工具）
- `tool_choice` 参数：`auto` vs `required` vs `none`
- 响应中的 `tool_calls` 字段结构
- 手动构建 tool message 返回给 LLM

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 4.1 | 手写 Function Calling | 不用任何 Agent 框架，纯用 `openai` 包手动实现一次完整的 tool calling 循环 |
| 4.2 | 观察协议 | 打印每一步的完整 JSON：请求体（含 tools 定义）、响应体（含 tool_calls）、工具执行结果、第二次请求（含 tool message） |
| 4.3 | 画流程图 | 手动画出一次 tool calling 的消息流转图：User → Assistant(tool_calls) → Tool → Assistant(最终回复) |
| 4.4 | 并行工具调用 | 问一个需要同时查多个城市天气的问题（如"北京和上海天气各如何？"），观察 LLM 能否在一个响应中返回多个 tool_calls |

### 产出物
- `raw_tool_calling.py` — 不依赖任何框架的手动实现
- 一份消息流转图

### 验收标准
- 能手写实现一次完整的 tool calling 循环
- 理解 LLM 返回的是"调用哪个函数的建议"而非"函数执行结果"
- 明白所有 Agent 框架底层都是这个循环

---

## 学习任务 5：用新版 LangChain 写 Agent（备选框架）

### 任务目标
掌握业界最主流框架 LangChain 的 Agent 写法，方便后续学习 RAG 和 LangGraph。

### 学习内容
- LangChain 新版 API（`create_agent`，2025 年改版）
- `@tool` 装饰器注册工具
- LangChain 的消息格式（`HumanMessage`、`AIMessage`、`ToolMessage`）
- 与 PydanticAI 的对比

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 5.1 | 安装 LangChain | `pip install langchain langchain-openai` |
| 5.2 | LangChain Agent | 用 `create_agent` 创建和 PydanticAI 同样功能的 Agent，对比代码量和可读性 |
| 5.3 | 框架对比 | 写一份简要对比：PydanticAI 的优势（类型安全、简洁）vs LangChain 的优势（生态全、社区大） |
| 5.4 | 工具迁移 | 把任务 2 中 PydanticAI 的 3 个工具迁移到 LangChain，确认行为一致 |

### 产出物
- `langchain_agent.py` — LangChain 版本的 Agent
- `framework_comparison.md` — 两个框架的使用体验对比

### 验收标准
- 能用 LangChain 写出与 PydanticAI 功能等价的 Agent
- 能判断什么场景用哪个框架

---

## 学习任务 6：综合实战 — 个人助理 Agent

### 任务目标
做一个真正有用的个人助理 Agent，整合本阶段所有技能。

### 功能需求

```
个人助理 Agent
==============
工具列表：
1. get_time() — 获取当前日期时间
2. get_weather(city: str) — 查询城市天气（用免费天气 API）
3. calculate(expression: str) — 数学计算
4. search_web(query: str) — 网页搜索
5. manage_todo(action: str, task: str = None) — 管理待办事项（add/list/done/delete）
6. translate(text: str, target_lang: str = "英文") — 翻译
7. set_reminder(task: str, minutes: int) — 设置提醒（倒计时）

能力要求：
- 用户说 "今天要做什么" 时自动查时间和待办
- 用户说 "帮我把 XXX 翻成英文" 时调翻译
- 用户说 "搜一下 XXX" 时调搜索
- 用户说 "30 分钟后提醒我开会" 时设置倒计时
- 所有工具调用失败时有优雅的降级
- 用 asyncio 实现，支持异步并发工具调用
```

### 技术要求
- 用 PydanticAI 实现（推荐）或 LangChain
- 至少 5 个工具（其中至少 2 个调用真实外部 API）
- 完整的异常处理和重试
- 工具调用日志（记录每次调用：时间、工具名、参数、耗时、成功/失败）
- `asyncio.gather` 支持并行调用多个工具

### 产出物
- `personal_assistant.py` — 完整的命令行个人助理
- 工具调用日志（文本文件自动记录）
- `README.md` 说明所有工具和使用方法

### 验收标准
- 运行 `python personal_assistant.py` 进入交互式对话
- 至少 5 个工具可用，Agent 自动选对工具
- 工具调用成功率 > 85%（10 个测试用例）
- 所有失败场景有优雅处理，不会崩溃
- 日志可追溯每次工具调用

---

## 推荐学习资源

| 资源 | 说明 |
|------|------|
| [PydanticAI 官方文档](https://ai.pydantic.dev/) | Agent 入门首选，文档极佳 |
| [PydanticAI Examples](https://github.com/pydantic/pydantic-ai) | 官方仓库含 bank_support、rag、sql_gen、flight booking 等完整示例 |
| [LangChain Quickstart](https://docs.langchain.com/oss/python/langchain/quickstart) | LangChain 新版 `create_agent` 快速上手 |
| [Anthropic Tool Use Course](https://github.com/anthropics/courses/tree/master/tool_use) | 理解 Tool Calling 底层原理 |
| [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) | `simple_conversational_agent.ipynb` 等入门教程 |
| [duckduckgo_search](https://pypi.org/project/duckduckgo-search/) | 免费网页搜索库，不需要 API Key |

---

## 学习节奏建议

| 天数 | 完成任务 | 产出 |
|------|---------|------|
| Day 1 | 任务 1：PydanticAI 跑通第一个 Agent | hello_agent.py |
| Day 2 | 任务 2：多工具 Agent | multi_tool_agent.py |
| Day 3 | 任务 3：工具调用健壮性 | robust_agent.py |
| Day 4 | 任务 4：理解底层机制 | raw_tool_calling.py |
| Day 5 | 任务 5：LangChain 备选框架 | langchain_agent.py |
| Day 6-7 | 任务 6：综合实战"个人助理 Agent" | personal_assistant.py |

---

## 阶段 2 完成后的你应该能

- [ ] 用 PydanticAI 或 LangChain 创建 Agent，注册工具
- [ ] 理解 Tool Calling 的完整消息流转（User → LLM tool_calls → Your Code → Tool Result → LLM Answer）
- [ ] 给 Agent 配多个工具，Agent 能根据用户意图自动选择
- [ ] 处理工具调用失败、参数错误、超时等异常场景
- [ ] 不依赖框架也能手写实现 Function Calling
- [ ] 完成"个人助理 Agent"项目，有 5 个以上可用工具

**全部打勾后，进入阶段 3：RAG 知识库问答。**
