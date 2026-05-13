# AIAgent开发工程师 — 小白从零学习计划

> 适用人群：听说过 Agent、RAG、向量数据库等名词，但不了解任何技术细节，几乎零基础。
> 目标：一步步从 "会用 ChatGPT" 变成 "能独立搭建并交付 Agent 系统"。

---

## 0. 前置阅读：这些名词到底是什么意思？

在开始写代码之前，先用大白话理解每个概念，避免后面学的时候"只知道怎么做，不知道为什么做"。

| 名词 | 一句话解释 | 类比 |
|------|-----------|------|
| **LLM（大语言模型）** | 就是 ChatGPT/GPT-4/Claude 背后的"大脑" | 一个读过很多书的毕业生，能回答各种问题 |
| **Token** | LLM 处理文本的最小单位，一个中文字≈2个token | 就像"字数"，但更细 |
| **Prompt（提示词）** | 你给 LLM 的输入指令 | 你给毕业生布置的任务说明书 |
| **Function Calling / Tool Calling** | 让 LLM 能调用外部工具（查数据库、搜网页、发邮件） | 给毕业生配了一部手机，他能打电话查东西 |
| **Agent（智能体）** | 能自主规划、调用工具、多步执行任务的 LLM 程序 | 不只是回答问题，而是能"做事"的 AI 助手 |
| **RAG（检索增强生成）** | 让 LLM 先查资料再回答，资料来源是你给的文档/知识库 | 考试时允许翻书作答 |
| **Embedding（向量嵌入）** | 把一段文字变成一串数字（向量），方便计算机比较相似度 | 给每本书贴一个数字标签，标签相近的书内容也相近 |
| **向量数据库** | 专门存储和检索这些数字向量的数据库 | 一个按内容相似度来搜书的图书馆目录 |
| **Memory（记忆）** | Agent 记住之前对话/操作的能力 | 和助手合作久了，他记住你的偏好 |
| **Multi-Agent（多智能体）** | 多个 Agent 分工协作完成复杂任务 | 一个团队：有人调研、有人写稿、有人审校 |

---

## 1. 学习路线总览

按真实社区中最成熟的路线，分 6 个阶段。每阶段都有**具体项目产出**，不只学概念。

```
阶段0: Python 基础           （2-4周） —— 会用 Python 写函数、调接口
阶段1: LLM 原理与 API 调用    （1-2周） —— 能调 OpenAI API 完成对话
阶段2: 第一个 Agent           （1-2周） —— LLM + 工具调用，做出会"做事"的程序
阶段3: RAG 知识库问答         （2-3周） —— 让 Agent 基于私有文档回答问题
阶段4: 复杂 Agent 系统        （3-4周） —— 多步骤、有记忆、有状态的 Agent
阶段5: 多 Agent 协作          （2-3周） —— 多个 Agent 分工配合
阶段6: 生产化与可视化部署     （2-3周） —— 把 Agent 真正上线用起来
```

**总时长**：每天 2 小时约 16-20 周，每天 4 小时约 10-12 周。

---

## 2. 阶段详解

---

### 阶段 0：Python 基础（2-4 周）

**为什么必须先学 Python？**
AI Agent 领域所有主流框架（LangChain、AutoGen、CrewAI、PydanticAI）都是 Python 库。不懂 Python 直接上框架 = 还没学会走路就想跑。

**学什么：**
1. Python 基本语法：变量、函数、类、列表、字典、循环、条件
2. **异步编程 async/await** —— Agent 框架大量使用异步，这是最大绊脚石
3. 类型注解（type hints）—— 现代 Agent 框架必备
4. 虚拟环境 venv、pip 包管理
5. 会用 requests 调 HTTP 接口

**推荐资源：**
- [Python 官方教程](https://docs.python.org/zh-cn/3/tutorial/) — 官方中文，免费
- [realpython.com](https://realpython.com/) — 实战教程，英文但质量极高
- B站搜 "Python 零基础入门" — 选一个播放量高的跟着敲

**验收标准：**
- 能独立写一个简单的命令行工具（如待办事项列表）
- 能写 async 函数并理解 await 的含义
- 能用 `pip install` 和 `venv` 管理环境

---

### 阶段 1：LLM 原理与 API 调用（1-2 周）

**为什么不能跳过？**
不先理解 LLM 是怎么工作的，后面 debug 会完全无从下手。理解 token、temperature 等概念是基本功。

**学什么：**
1. Token 是什么，为什么有上下文窗口限制
2. System Prompt vs User Prompt 的区别
3. Temperature、top_p 等采样参数怎么调
4. 调用 OpenAI 兼容 API（Python 代码）
5. 结构化输出：让 LLM 稳定输出 JSON

**动手项目：** "结构化问答助手"
- 输入一个问题，LLM 返回一个 JSON（包含：回答、信心分数、依据）
- 加入字段校验，输出格式错误时自动重试

**推荐资源：**
- [OpenAI API 文档](https://platform.openai.com/docs/overview) — 必读官方文档
- GitHub: `https://github.com/NirDiamant/Prompt_Engineering` — 提示词工程大全
- GitHub: `https://github.com/NirDiamant/GenAI_Agents` — 从 `simple_conversational_agent.ipynb` 开始看

**验收标准：**
- 能写代码调 LLM API 完成一次对话
- 能让 LLM 稳定输出可解析的 JSON
- 理解 token 消耗和成本

**成本提示：**
用 gpt-4o-mini 做开发测试，1000 个 token 才几分钱。别一上来就用最贵的模型。

---

### 阶段 2：第一个 Agent（1-2 周）

**这阶段做什么？**
给 LLM "配工具"——让它不仅能说话，还能做事（查天气、搜网页、算数学）。

**推荐入门框架：PydanticAI**
为什么是它？代码最简洁，概念最少，类型安全，官方文档质量极高。5 行代码就能跑起来：

```python
from pydantic_ai import Agent

agent = Agent('openai:gpt-4o-mini', instructions='回答要简洁。')
result = agent.run_sync('什么是 AI Agent？')
print(result.output)
```

**学什么：**
1. Tool Calling 原理：LLM 怎么知道该调哪个工具
2. 定义工具函数 + 注册给 Agent
3. 工具调用结果返回给 LLM 继续对话
4. 错误处理：工具调用失败怎么办
5. 参数校验：LLM 传错参数怎么兜底

**动手项目：** "个人助理 Agent"
- 工具1：获取当前时间
- 工具2：简单计算器
- 工具3：网页搜索（用 `duckduckgo_search` 库）
- 场景：用户问"今天几号？帮我算 12345×6789，再搜一下最近的 AI 新闻"

**推荐资源：**
- [PydanticAI 官方文档](https://ai.pydantic.dev/) — 入门首选
- GitHub: `https://github.com/NirDiamant/GenAI_Agents` — `tool_calling_agent.ipynb`
- [LangChain Quickstart](https://docs.langchain.com/oss/python/langchain/quickstart) — 如果想用 LangChain

**备选框架：新版 LangChain**
```python
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """查询城市天气"""
    return f"{city}今天晴天，25°C"

agent = create_agent(
    model="openai:gpt-4o-mini",
    tools=[get_weather],
    system_prompt="你是一个有用的助手",
)
result = agent.invoke({"messages": [{"role": "user", "content": "北京天气怎么样？"}]})
```

**验收标准：**
- Agent 能自动选择合适的工具并调用
- 工具调用失败后有降级处理
- 工具调用成功率 > 90%

---

### 阶段 3：RAG 知识库问答（2-3 周）

**为什么这阶段很重要？**
企业中 80% 的 Agent 应用都是 RAG 模式——让 AI 基于公司内部文档回答。这是面试必考。

**学什么：**
1. RAG 完整流程：文档 → 切分 → Embedding → 存向量库 → 检索 → 生成
2. 文档加载与清洗（PDF、TXT、Markdown）
3. 文档切块策略（固定长度 vs 语义切分）
4. Embedding 模型选型（OpenAI vs 开源模型）
5. 向量数据库（从轻量的 ChromaDB 开始）
6. 检索策略：Top-K、相似度阈值、重排序
7. 引用溯源：回答里标注信息来源

**动手项目：** "本地知识库问答系统"
- 把你的学习笔记/文档喂进去
- 问"第1周学了什么？"，Agent 能准确回答并标出来源
- 加入评测集（50 条问答），统计准确率

**技术选型：**
| 组件 | 推荐（入门） | 进阶 |
|------|-------------|------|
| 向量数据库 | ChromaDB（零配置） | Milvus / pgvector |
| Embedding | OpenAI `text-embedding-3-small` | BGE / Jina |
| 文档解析 | PyPDF2 / markdown | Unstructured.io |
| 检索框架 | LangChain RAG 模块 | LlamaIndex |

**推荐资源：**
- GitHub: `https://github.com/NirDiamant/RAG_Techniques` — **22 种 RAG 技术详解**，从 Naive RAG 到 Agentic RAG
- [ChromaDB 文档](https://docs.trychroma.com/) — 5 分钟上手向量库
- GitHub: `https://github.com/NirDiamant/GenAI_Agents` — `rag_tutorial.ipynb`

**验收标准：**
- 能上传 PDF/文档并基于内容问答
- 回答能追溯到具体文档片段
- 评测集准确率 > 70%（朴素 RAG）

---

### 阶段 4：复杂 Agent 系统（3-4 周）

**这阶段学什么？**
从"一问一答"升级到"多步骤执行"，Agent 能记住上下文，能反思纠错。

**核心概念：**
1. **状态图编排（LangGraph）**：Agent 不是一条直线执行，而是有分支、有循环的状态机
2. **记忆系统**：短期记忆（当前对话）、长期记忆（跨会话用户偏好）
3. **Plan-Act-Reflect 循环**：先规划 → 执行 → 检查结果 → 不行就重试
4. **Human-in-the-loop**：关键操作让人类确认后再执行

**动手项目：** "多步骤任务 Agent"
- 场景：用户说"帮我整理本周的工作内容并生成周报"
- Agent 步骤：获取本周任务列表 → 分类整理 → 生成 Markdown 周报 → 让用户确认 → 保存

**推荐资源：**
- GitHub: `https://github.com/NirDiamant/GenAI_Agents` 中的：
  - `customer_support_agent_langgraph.ipynb` — 多步骤客服 Agent
  - `memory-agent-tutorial.ipynb` — 记忆系统（语义+情景+过程记忆）
- [LangGraph 官方文档](https://langchain-ai.github.io/langgraph/)
- [LangChain Academy](https://github.com/langchain-ai/langchain-academy) — 官方学习课程

**验收标准：**
- Agent 能按步骤自动完成一个复杂任务
- 执行过程可追踪、可回放
- 中间步骤出错能自动重试或请求人类帮助

---

### 阶段 5：多 Agent 协作（2-3 周）

**为什么需要多 Agent？**
单个 Agent 处理复杂任务容易"分心"。多 Agent 像团队一样：有人专门研究、有人写代码、有人检查质量——各司其职，产出更高。

**推荐框架：CrewAI**
概念最直观：定义 Agent 角色 → 分配 Task → 组成 Crew → 执行 Flow。

```bash
pip install crewai
crewai create crew my-first-crew
```

**学什么：**
1. 角色分工模式：研究员 + 写手 + 审查员
2. Agent 间信息传递与依赖
3. 顺序执行 vs 并行执行
4. 冲突解决：两个 Agent 意见不一怎么办

**动手项目：** "内容创作团队"
- 研究员 Agent：搜索给定主题的最新资料
- 撰稿 Agent：根据研究结果写文章
- 编辑 Agent：审校文章，提出修改意见
- 流程：研究 → 撰稿 → 编辑反馈 → 撰稿修改 → 定稿

**推荐资源：**
- [CrewAI 官方文档](https://docs.crewai.com/quickstart)
- GitHub: `https://github.com/NirDiamant/GenAI_Agents` — `multi_agent_collaboration_system.ipynb`
- GitHub: `https://github.com/crewAIInc/crewAI`

**备选框架：AutoGen（微软）**
功能更强但学习曲线更陡，适合有经验的开发者。
- GitHub: `https://github.com/microsoft/autogen`
- 关键 tutorial: `research_team_autogen.ipynb`（在 GenAI Agents 仓库中）

**验收标准：**
- 至少 2 个 Agent 协作完成一个任务
- 能对比单 Agent vs 多 Agent 的质量差异
- 协作流程可可视化展示

---

### 阶段 6：生产化与可视化部署（2-3 周）

**这阶段做什么？**
前面写的都是脚本，现在要把它变成一个真正可以给别人用的"产品"。

**推荐平台：Dify**
开源可视化 Agent 平台，拖拽就能搭建工作流。支持自部署，从可视化入门再过渡到代码。
- GitHub: `https://github.com/langgenius/dify`
- [Dify 官方文档](https://docs.dify.ai/zh-hans)

**学什么（按优先级）：**
1. **Dify 可视化搭建** — 最快做出可演示产品
2. **Docker 容器化部署** — 让服务能在任何机器上跑
3. **API 封装** — FastAPI 把 Agent 包装成 HTTP 接口
4. **可观测性** — LangSmith 追踪每次调用的耗时/成功率/成本
5. **评测体系** — 建立测试集，持续监控 Agent 输出质量
6. **安全基础** — Prompt Injection 防护、敏感信息脱敏

**动手项目：** "三个可交付项目"
1. 企业知识库问答系统（RAG）
2. 工单自动处理 Agent（分类、分派、回复建议）
3. 代码助手 Agent（代码审查、Bug 建议）

**验收标准：**
- 项目有完整的 README 和部署文档
- 新环境能按文档一键启动
- 有评测数据和效果对比

---

## 3. 框架选择建议

市面上框架很多，新人容易选择困难。按这个顺序来：

```
第1步：PydanticAI   → 最简入门，理解 Agent 核心概念（阶段2）
第2步：LangChain     → 生态最全，学习 RAG 和工具链（阶段3）
第3步：LangGraph     → 掌握复杂 Agent 状态编排（阶段4）
第4步：CrewAI        → 学习多 Agent 协作（阶段5）
第5步：Dify          → 可视化部署，快速交付（阶段6）
```

> 不要同时学 5 个框架！每个阶段专注一个。

---

## 4. 新手最容易踩的 8 个坑

| # | 坑 | 怎么避免 |
|---|-----|---------|
| 1 | **跳过 LLM 原理直接学框架** | 先花 1 周读 OpenAI API 文档，理解 token/temperature/function calling |
| 2 | **混淆 LangChain 新旧版本** | 2025 年 LangChain 大改版（`create_agent`），网上很多教程已过时。锁定[官方文档](https://docs.langchain.com/)为唯一真相源 |
| 3 | **不学 async/await** | Agent 框架大量使用异步。先花 2 天专门练习异步编程 |
| 4 | **API Key 写在代码里传 GitHub** | 务必用 `.env` 文件 + `.gitignore`。一旦泄露会被盗刷 |
| 5 | **贪多嚼不烂** | 别同时学 LangChain + AutoGen + CrewAI + LlamaIndex。一次一个 |
| 6 | **从不做评测** | Agent 输出是非确定性的，必须持续测试。从简单的准确率统计开始 |
| 7 | **追求大模型浪费钱** | 开发用 `gpt-4o-mini`（便宜 90%），上线再切大模型 |
| 8 | **没有 Human-in-the-loop** | 别让 Agent 直接操作生产数据。先"建议"再由人"确认" |

---

## 5. 每日学习节奏建议

| 时间段 | 做什么 |
|--------|--------|
| **周一~周三** | 学习新概念 + 写最小原型代码 |
| **周四~周五** | 补功能 + 写测试 + 修 Bug |
| **周六** | 写文档、录演示、做复盘 |
| **周日** | 查漏补缺 + 规划下周 |

**每周必须有至少一个"可运行演示"**，不要只记笔记不写代码。

---

## 6. 必收藏的 GitHub 仓库

| 仓库 | 说明 | 适合阶段 |
|------|------|----------|
| [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) | **52+ 个 Jupyter Notebook 教程**，从入门到多 Agent | 阶段1-5 |
| [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | 22 种 RAG 技术详解 | 阶段3 |
| [NirDiamant/Prompt_Engineering](https://github.com/NirDiamant/Prompt_Engineering) | 提示词策略大全 | 阶段1 |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | 类型安全的 Agent 框架 | 阶段2 |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | LangChain 主仓库 | 阶段2-4 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Agent 状态编排引擎 | 阶段4 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 多 Agent 协作框架 | 阶段5 |
| [langgenius/dify](https://github.com/langgenius/dify) | 可视化 Agent 平台 | 阶段6 |
| [microsoft/autogen](https://github.com/microsoft/autogen) | 微软多 Agent 框架 | 阶段5 |
| [langchain-ai/langchain-academy](https://github.com/langchain-ai/langchain-academy) | LangChain 官方课程 | 阶段4 |
| [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) | AI Agent 资源总汇 | 全阶段 |

---

## 7. 你可以立刻开始的第一步（今天）

1. 打开终端，确认 Python 已安装：`python --version`（需要 3.10+）
2. 创建项目文件夹，初始化虚拟环境：
   ```bash
   mkdir agent-learning-lab
   cd agent-learning-lab
   python -m venv .venv
   ```
3. 访问 [OpenAI Platform](https://platform.openai.com/) 注册并获取 API Key
4. 安装 PydanticAI：`pip install pydantic-ai`
5. 写 5 行代码跑通你的第一个 Agent（见阶段2示例）
6. 开始记录 `metrics.md`，从第一天起追踪：调用次数、成功率、延迟、成本

---

## 8. 验收标准总结

| 阶段 | 核心验收标准 |
|------|-------------|
| 0 Python | 能写 async 函数，理解类型注解 |
| 1 LLM | 能调 API，LLM 稳定输出 JSON |
| 2 Agent | Agent 能自动选工具调用，成功率 > 90% |
| 3 RAG | 知识库问答能追溯到原文，准确率 > 70% |
| 4 复杂 Agent | 多步骤任务可自动完成，执行可追踪 |
| 5 多 Agent | 2+ Agent 协作，对比单 Agent 有明显提升 |
| 6 生产化 | 3 个可交付项目，有完整文档和评测数据 |

---

> 最终标准：你不是"会用 AI 工具"，而是"能把 Agent 做成稳定可交付系统"的工程师。
>
> 开始行动吧。从今天起，每天写一点代码，每周交付一个小项目。
