# 阶段1：LLM 原理与 API 调用 — 学习任务说明文档

> **定位**：从"会写 Python"到"能稳定调用大模型"。理解 LLM 的核心概念，掌握 API 调用的完整流程。
> **前置条件**：完成阶段 0（Python 基础），能写 async 函数、用 Pydantic 定义模型、发 HTTP 请求。
> **总时长**：每天 2 小时，约 1-2 周完成。

---

## 学习前必读：这些概念是 Agent 开发的基石

| 概念 | 你必须理解到什么程度 |
|------|---------------------|
| **Token** | 能估算一段中文大概消耗多少 token，知道上下文窗口是什么 |
| **System Prompt vs User Prompt** | 知道 system 是"设定角色"，user 是"当前问题" |
| **Temperature / Top-P** | 能解释为什么 Agent 工具调用要设 `temperature=0`，创意写作要设 `temperature=0.9` |
| **Function Calling** | 理解 LLM 不是"执行"工具，而是"建议调用哪个工具"——真正执行代码的是你的 Python 程序 |
| **结构化输出** | 能让 LLM 稳定输出 JSON，输出格式错误时能自动校验和重试 |

---

## 学习任务 1：注册 API + 第一次调用

### 任务目标
拿到 API Key，用 Python 代码调用 LLM，得到第一个回复。

### 学习内容
- OpenAI 兼容 API 的鉴权方式（Bearer Token）
- `chat/completions` 接口的请求格式
- `messages` 列表的结构：`[{"role": "system/user/assistant", "content": "..."}]`
- 响应解析：`response.choices[0].message.content`

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 1.1 | 注册获取 API Key | 访问 [platform.openai.com](https://platform.openai.com/) 注册，创建 API Key。**立即**在平台充值 $5（最低额度，够用很久）。**绝不要把 Key 写在代码里。** |
| 1.2 | .env 文件管理 Key | 安装 `python-dotenv`，创建 `.env` 文件写入 `OPENAI_API_KEY=sk-xxx`，`.gitignore` 中加上 `.env`。代码中用 `os.getenv("OPENAI_API_KEY")` 读取 |
| 1.3 | 第一次调用 | 安装 `openai` 包，写 `first_call.py`：发送 `"你好，请用一句话介绍你自己"`，打印 LLM 的回复 |
| 1.4 | 多轮对话 | 扩展代码：连续发送 3 条消息，每次把历史 messages 都带上。观察 LLM 如何"记住"之前的对话 |

### 产出物
- `first_call.py` — 完成单轮和多轮对话
- `.env` 文件 + `.gitignore` — 安全管理 API Key
- `requirements.txt` 含 `openai` 和 `python-dotenv`

### 验收标准
- 能成功调用 LLM API 并获得回复
- API Key 写在 `.env` 中，代码不硬编码
- 理解 messages 列表是"对话历史"——每次请求都要把历史带上

---

## 学习任务 2：理解 Token 与上下文窗口

### 任务目标
理解 Token 是什么，能计算 Token 数，避免发送超长文本导致截断。

### 学习内容
- Token 不是"字"——一个中文字 ≈ 2 token，一个英文单词 ≈ 1.3 token
- 上下文窗口（Context Window）：不同模型有不同的上限（如 gpt-4o=128K tokens）
- 输入 Token + 输出 Token 都算在窗口内
- 为什么需要"Token 管理"：历史对话越长，留给回答的空间越少

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 2.1 | 安装 tiktoken | `pip install tiktoken`，用它计算一段中英文混合文本的 token 数 |
| 2.2 | Token 计数器 | 写函数 `count_tokens(text: str, model: str = "gpt-4o") -> int`，返回 token 数 |
| 2.3 | 消息列表统计 | 写函数 `count_messages_tokens(messages: list[dict]) -> int`，计算整个对话历史的 token 数 |
| 2.4 | 截断策略 | 实现 `truncate_messages(messages, max_tokens=8000)`：保留最近的 N 条消息，确保总 token 不超过上限。保留 system prompt 不删 |
| 2.5 | 成本计算 | 每轮对话后从 `response.usage` 中获取 `prompt_tokens` 和 `completion_tokens`，按模型价格计算并累计。打印 "本次花费: $0.00032，累计花费: $0.00150" |

### 产出物
- `token_manager.py` — 包含上述所有函数
- 一个成本追踪日志

### 验收标准
- 能估算一段文字的 token 数（误差 < 20%）
- 能自动截断超长对话历史
- 知道每次调用的成本，不浪费钱

### 成本参考（开发阶段全程极便宜）
| 模型 | 输入 1K tokens | 输出 1K tokens |
|------|---------------|----------------|
| gpt-4o-mini | $0.00015 | $0.0006 |
| gpt-4o | $0.0025 | $0.01 |
| claude-3-haiku | $0.00025 | $0.00125 |

> **开发调试全程用 gpt-4o-mini**，每天 1 小时练习花不了 $0.1。

---

## 学习任务 3：System Prompt 与采样参数

### 任务目标
掌握 System Prompt 的设计和采样参数（temperature、top_p）的调优。

### 学习内容
- System Prompt 的作用：设定角色、行为边界、输出格式要求
- 好的 System Prompt vs 差的 System Prompt
- Temperature：0=每次一样(适合工具调用)，1=每次不同(适合创意)
- Top-P（nucleus sampling）：和 temperature 二选一调，不要两个同时调
- `max_tokens` / `stop` 参数

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 3.1 | 角色扮演 | 写 3 个不同的 system prompt，分别让 LLM 扮演"毒舌影评人""幼儿园老师""技术文档写手"，对同一部电影写评价。对比输出风格 |
| 3.2 | Temperature 实验 | 同一 prompt 分别用 temperature=0 / 0.5 / 1.0 / 1.5 各调用 3 次。统计相同 temperature 下输出的相似度，以及不同 temperature 下的差异度 |
| 3.3 | Few-shot 示例 | 在 system prompt 中给出 3 个"输入→输出"示例，然后测试新输入。对比有示例 vs 无示例的输出质量 |
| 3.4 | 输出约束 | 设计 system prompt 要求 LLM 回复时：不超过 50 字、使用 Markdown 格式、只回答"是"或"否"开头。测试 LLM 遵守规则的程度 |

### 产出物
- `prompt_lab.py` — 包含上述实验的代码
- 一份实验报告（Markdown）记录：不同 temperature 的表现差异、few-shot 的效果

### 验收标准
- 能写出在不同场景下有效的 system prompt
- 理解 temperature=0 对 Agent 工具调用是必须的
- 知道 few-shot 是提升输出质量的最简单技巧

---

## 学习任务 4：结构化输出

### 任务目标
让 LLM 稳定输出可解析的 JSON，并自动校验和重试。这是 Agent 开发的核心能力——LLM 的输出必须能被程序读懂。

### 学习内容
- OpenAI `response_format={"type": "json_object"}` — 强制 JSON 输出
- JSON Schema 定义与校验
- Pydantic 从 JSON 字符串自动解析
- 输出校验失败时的重试策略

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 4.1 | 基础 JSON 输出 | 用 `response_format={"type": "json_object"}` 让 LLM 分析一段产品描述，输出 `{"product": "...", "features": [...], "price_range": "..."}` |
| 4.2 | Pydantic 校验 | 用 Pydantic `BaseModel` 定义输出结构，LLM 返回的 JSON 字符串用 `model_validate_json()` 解析。格式错误时自动重试（最多 3 次） |
| 4.3 | 信息提取器 | 从一段混乱的会议记录中提取：参与者列表、决议事项、待办事项（含负责人和截止日期）。输出结构化 JSON |
| 4.4 | 鲁棒性测试 | 故意给 LLM 一段模糊/不完整的文本，观察输出。完善 retry 逻辑：格式错误重试 → 重试时 prompt 中加入上一次的错误信息 |

### 产出物
- `structured_output.py` — 健壮的结构化输出封装，含 Pydantic 校验 + 重试
- 至少 2 个 Pydantic 输出模型定义

### 验收标准
- LLM 输出 JSON 解析成功率 > 95%
- 格式错误时自动重试，重试时错误信息反馈给 LLM
- 能用 Pydantic 校验字段类型和必填项

---

## 学习任务 5：流式输出 (Streaming)

### 任务目标
实现流式输出——用户看到文字一个一个字往外蹦，而不是傻等。

### 学习内容
- SSE（Server-Sent Events）协议原理
- OpenAI `stream=True` 参数
- 逐 chunk 处理：`response` → `delta.content`
- `async for` 消费流式响应

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 5.1 | 同步流式 | 用 `stream=True` 调用 OpenAI API，for 循环逐块打印内容 |
| 5.2 | 异步流式 | 用异步方式实现流式输出，`async for chunk in stream` |
| 5.3 | 流式 + 累积 | 流式打印的同时，把所有 chunk 拼接成完整回复。结束后打印完整回复的 token 数和耗时 |
| 5.4 | 打字机效果 | 实现每打印一个 chunk 后 `await asyncio.sleep(0.02)`，模拟打字机效果 |

### 产出物
- `streaming.py` — 异步流式输出封装
- 体验打字机效果

### 验收标准
- 能实现异步流式输出
- 流式过程中能同时收集完整回复

---

## 学习任务 6：综合实战 — 结构化问答助手

### 任务目标
整合本阶段所有技能，做一个能用的"结构化问答助手"。

### 功能需求

```
结构化问答助手
================
用户可以问任何问题，LLM 始终返回以下 JSON 结构：
{
  "answer": "简洁回答",
  "summary": "一句话总结",
  "confidence": 0.85,        // 0-1 之间的信心分数
  "follow_up_questions": [   // 3 个可能的后续问题
    "问题1", "问题2", "问题3"
  ],
  "sources_used": ["推理依据1", "推理依据2"]
}

额外要求：
- 流式输出 "正在思考..." 的进度提示
- 输出格式错误时自动重试
- 显示每次调用的 token 消耗和成本
- 支持连续多轮对话（带历史上下文）
```

### 技术要求
- 用 `asyncio` 实现异步
- 用 Pydantic 定义输入输出模型
- 用 `response_format={"type": "json_object"}` 强制 JSON
- 用 `tiktoken` 管理 token，历史消息超过窗口时自动截断
- 流式输出打字机效果
- 异常处理：网络错误重试 3 次、API 限流等待重试

### 产出物
- `qa_assistant.py` — 完整的命令行问答助手
- Prompt 模板库（至少 3 个不同场景的 system prompt）
- `README.md` 说明使用方法

### 验收标准
- 运行 `python qa_assistant.py` 能开始交互式问答
- 每次回答都是可解析的 JSON
- 连续对话中 LLM 能记住上下文
- 成本统计实时可见

---

## 推荐学习资源

| 资源 | 说明 |
|------|------|
| [OpenAI API 文档](https://platform.openai.com/docs/overview) | 必读，理解每个参数的含义 |
| [Anthropic Courses](https://github.com/anthropics/courses) | API 基础 + 提示词工程交互式教程，21k stars |
| [Prompt Engineering Guide](https://www.promptingguide.ai/) | 涵盖所有提示词技术，免费 |
| [NirDiamant/Prompt_Engineering](https://github.com/NirDiamant/Prompt_Engineering) | 提示词策略大全 |
| [tiktoken](https://github.com/openai/tiktoken) | OpenAI 官方的 Token 计算工具 |

---

## 学习节奏建议

| 天数 | 完成任务 | 累计 |
|------|---------|------|
| Day 1 | 任务 1：注册 API + 第一次调用 | 已能对话 |
| Day 2 | 任务 2：Token 与上下文窗口 | 会管成本 |
| Day 3 | 任务 3：System Prompt 与采样参数 | 能调优 |
| Day 4 | 任务 4：结构化输出（重点） | 输出可控 |
| Day 5 | 任务 5：流式输出 | 体验优化 |
| Day 6-7 | 任务 6：综合实战"结构化问答助手" | 完整作品 |

---

## 阶段 1 完成后的你应该能

- [ ] 用 Python 异步调用 LLM API，获得流式/非流式回复
- [ ] 管理 Token 消耗，自动截断超长对话
- [ ] 设计有效的 System Prompt 控制 LLM 行为
- [ ] 让 LLM 稳定输出结构化 JSON，并自动校验重试
- [ ] 理解 temperature 对输出的影响，知道不同场景该设什么值
- [ ] 完成"结构化问答助手"项目，可演示

**全部打勾后，进入阶段 2：第一个 Agent（Tool Calling）。**
