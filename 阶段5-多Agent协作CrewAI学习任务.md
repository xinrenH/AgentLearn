# 阶段5：多 Agent 协作（CrewAI）— 学习任务说明文档

> **定位**：像管理团队一样管理 Agent——有人专门研究、有人写稿、有人检查质量。多 Agent 协作能处理单个 Agent 搞不定的复杂任务。
> **前置条件**：完成阶段 4（LangGraph 复杂 Agent），理解状态图、工具调用、记忆系统。
> **总时长**：每天 2 小时，约 2-3 周完成。

---

## 学习前必读：单 Agent vs 多 Agent

**单 Agent 的问题**：
- 一个 Agent 同时做研究、写作、审校 → 容易"分心"，质量参差不齐
- 一个超长的 system prompt 塞满所有规则 → LLM 难以遵循
- 复杂任务缺乏"专业分工"

**多 Agent 的优势**：
- 每个 Agent 只聚焦一个角色（单一职责原则）
- 像真实团队一样：研究员→撰稿人→编辑→发布
- 各 Agent 可以用不同的模型（省钱：研究员用 cheap model，编辑用 strong model）
- 可并行执行（研究和数据采集同时做）

**关键认知**：多 Agent 不是银弹。简单任务（查天气、回答问题）用单 Agent 够用。只有复杂、多步骤、需要不同专长的任务才值得用多 Agent。

---

## 学习任务 1：CrewAI 快速上手

### 任务目标
用 CrewAI 跑通第一个多 Agent 协作任务。CrewAI 概念最直观，适合入门。

### 核心概念
- **Agent**：定义一个角色（role、goal、backstory）
- **Task**：分配具体任务（description、expected_output、assigned_agent）
- **Crew**：把 Agent + Task 组合成团队，定义执行模式（sequential / parallel）
- **Flow**：事件驱动的流程编排（比 Crew 更灵活）
- **Tool**：Agent 可用的工具（和单 Agent 一样）

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 1.1 | 安装 CrewAI | `pip install crewai crewai-tools` |
| 1.2 | 第一个 Crew | 创建 2 个 Agent：`researcher`（研究员）+ `writer`（撰稿人），1 个 Task：搜索"量子计算最新进展"并写一篇 500 字总结。用 `sequential` 模式执行 |
| 1.3 | 观察执行过程 | 打开 CrewAI 的 verbose 日志，观察：研究员先搜索 → 研究员输出传给撰稿人 → 撰稿人基于研究结果写稿 |
| 1.4 | 对比单 Agent | 用单 Agent 完成同一个任务，对比输出质量和执行时间 |

### 产出物
- `first_crew.py` — 第一个多 Agent 团队
- 执行日志
- 单 Agent vs 双 Agent 对比报告

### 验收标准
- CrewAI 团队能跑通 sequential 执行
- 研究员的结果确实传递给了撰稿人
- 理解 Agent→Task→Crew 三层概念

---

## 学习任务 2：角色分工与团队设计

### 任务目标
学会设计 Agent 角色，给不同 Agent 分配不同专长和工具。

### 学习内容
- 角色设计原则：单一职责、明确边界
- Role / Goal / Backstory 怎么写最有效
- 工具的专有分配：研究员有搜索工具，编辑没有（只能看不能搜）
- 模型分层：研究员用 cheap model（gpt-4o-mini），编辑用 strong model（gpt-4o）

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 2.1 | 设计 4 角色团队 | (1) 需求分析师（分析用户需求，输出需求文档）(2) 研究员（搜索技术方案）(3) 架构师（输出系统设计方案）(4) 审查员（检查方案的可行性/成本/风险） |
| 2.2 | 工具分配 | 研究员分配 `SerperDevTool`（搜索）；需求分析师分配 `FileReadTool`（读已有文档）；架构师不分配搜索工具（基于前两者输出做设计） |
| 2.3 | 模型分层 | 需求分析师和研究员用 `gpt-4o-mini`，架构师和审查员用 `gpt-4o`。统计总成本 |
| 2.4 | 角色冲突测试 | 故意让两个 Agent 角色有重叠（如"研究员"和"分析师"都负责搜索），观察混乱现象。然后明确边界后重跑 |

### 产出物
- `designed_crew.py` — 精心设计的多角色团队
- 角色定义文档（YAML 格式，CrewAI 推荐方式）
- 成本对比：统一用 gpt-4o vs 分层用不同模型

### 验收标准
- 能设计 3 个以上职责清晰的 Agent 角色
- 不同 Agent 分配不同工具和模型
- 模型分层有效降低成本
- 角色边界清晰，没有重复劳动

---

## 学习任务 3：顺序执行 vs 并行执行

### 任务目标
理解不同执行模式的区别和适用场景。

### 学习内容
- **Sequential**：Agent 按顺序执行，后一个拿到前一个的输出。适合"流水线"型任务
- **Parallel**：多个 Agent 同时执行，互不依赖。适合"分头行动"型任务
- **混合模式**：先分头并行研究，再汇总给执行者
- 什么时候用并行：任务之间无依赖关系时
- 并行带来的问题：结果不一致怎么办

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 3.1 | Sequential 模式 | 同一个任务用 sequential 执行，记录总耗时 |
| 3.2 | Parallel 模式 | 同一任务中独立步骤改为 parallel 执行，记录总耗时。计算加速比 |
| 3.3 | 混合模式 | 任务：分析 3 家竞品公司。3 个研究员并行分别研究 3 家公司 → 结果汇总给 1 个分析师做对比报告 |
| 3.4 | 并行冲突处理 | 3 个并行 Agent 对同一事实给出了不同结论。汇总 Agent 如何处理冲突：标注分歧、请求澄清、投票决定 |

### 产出物
- `execution_modes.py` — 3 种执行模式的对比实现
- 性能报告：3 种模式的耗时、token 消耗、输出质量对比

### 验收标准
- 能根据任务特点选择 sequential 或 parallel
- 能实现混合执行模式
- 并行冲突有合理的处理机制

---

## 学习任务 4：CrewAI Flow（事件驱动流程）

### 任务目标
掌握 CrewAI 的 Flow API——比 Crew 更灵活的事件驱动编排。

### 学习内容
- `@start()` 和 `@listen()` 装饰器
- Flow 状态管理（`self.state`）
- 条件路由：根据状态决定下一步调哪个 Crew
- Flow 与 Crew 的关系：一个 Flow 里可以触发多个 Crew

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 4.1 | 第一个 Flow | 用 `@start()` 定义入口，`@listen()` 链接后续步骤，实现和任务 1 同样逻辑的 Flow |
| 4.2 | 条件路由 | Flow 中根据用户输入类型：简单问题 → 单 Agent 回答；复杂问题 → 触发多 Agent Crew |
| 4.3 | 多 Crew 编排 | Flow 中有 2 个 Crew：`ResearchCrew` 和 `PublishCrew`。先触发 Research → 根据研究结果决定是否需要 Publish |
| 4.4 | Flow 可视化 | 用 `crewai run` 运行，查看 Flow 的执行轨迹 |

### 产出物
- `crew_flow.py` — 一个含条件路由和多 Crew 的 Flow

### 验收标准
- 能用 Flow API 编排多个 Crew
- 能根据状态做条件路由
- 理解 Flow 和 Crew 的层级关系

---

## 学习任务 5：AutoGen 入门（备选框架）

### 任务目标
了解微软的 AutoGen 框架，理解它与 CrewAI 的设计哲学差异。

### 学习内容
- AutoGen 的事件驱动模型（比 CrewAI 更底层）
- `AssistantAgent` 和 `RoundRobinGroupChat`
- 与 CrewAI 的关键区别：CrewAI 是角色扮演，AutoGen 是事件驱动对话
- 什么时候选 AutoGen：需要更灵活的对话控制、分布式部署

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 5.1 | 安装 AutoGen | `pip install autogen-agentchat autogen-ext[openai]` |
| 5.2 | 第一个 AutoGen 团队 | 创建 2 个 `AssistantAgent`，用 `RoundRobinGroupChat` 让它们轮流对话解决问题 |
| 5.3 | 同一任务对比 | 用 AutoGen 实现 CrewAI 任务 1 中的"研究+写稿"，对比：代码复杂度、执行效果、可控性 |

### 产出物
- `autogen_demo.py` — AutoGen 版本的多 Agent 协作
- `crewai_vs_autogen.md` — 两个框架的使用对比

### 验收标准
- 能跑通 AutoGen 的多 Agent 对话
- 理解 CrewAI 和 AutoGen 的核心设计差异
- 能根据场景选择合适的框架

---

## 学习任务 6：综合实战 — 智能内容创作团队

### 任务目标
做一个完整的多 Agent 内容创作系统，从选题到发布全流程。

### 功能需求

```
智能内容创作团队（Multi-Agent）
==============================
团队角色（4 Agent + 1 Human-in-the-loop）：

1. 选题策划师 (Topic Planner)
   - 工具：网页搜索、趋势分析
   - 职责：分析当前热点，提出 3 个选题方向
   - 输出：选题列表（含标题、角度、预期受众）

2. 研究员 (Researcher)
   - 工具：网页搜索、文档检索
   - 职责：针对选定选题搜集资料、数据、案例
   - 输出：研究摘要（含数据来源、关键引用）

3. 内容撰稿人 (Content Writer)
   - 工具：无（基于研究结果创作）
   - 职责：基于研究结果撰写完整文章
   - 输出：Markdown 格式文章（含标题、导语、正文、结论）

4. 编辑审校 (Editor)
   - 模型：gpt-4o（最强模型，审校质量要求高）
   - 职责：检查文章的事实准确性、逻辑连贯性、语言流畅度
   - 输出：修改建议列表 + 修改后版本

5. 人类决策节点（Human-in-the-loop）
   - 选题阶段：从 3 个选题中选 1 个
   - 终稿阶段：确认发布 or 要求修改

执行流程：
1. 用户输入主题 → 选题策划师生成 3 个选题
2. 人工选择 1 个选题
3. 研究员搜集资料
4. 内容撰稿人撰写初稿
5. 编辑审校 + 提出修改意见
6. 撰稿人根据意见修改（最多 2 轮）
7. 人工最终审核
8. 保存为 Markdown 文件 + 发布
```

### 技术要求
- CrewAI 实现多 Agent 协作
- 至少 2 处 Human-in-the-loop
- 执行过程完整日志
- 文章保存为 Markdown
- 评测：生成 3 篇文章，人工打分（1-5）对比单 Agent 输出的质量

### 产出物
- `content_team/` 项目目录：
  - `agents.yaml` — Agent 角色定义
  - `tasks.yaml` — Task 定义
  - `crew.py` — Crew 组装
  - `flow.py` — Flow 编排
  - `main.py` — 交互入口
  - `outputs/` — 生成的文章和日志
- 对比报告：多 Agent vs 单 Agent 的 3 篇文章质量评分

### 验收标准
- 4 个 Agent 协作完成一篇完整文章
- 人工介入节点正常工作
- 文章质量明显优于单 Agent 输出（有评分证据）
- 执行日志可追溯每个 Agent 的输入输出

---

## 推荐学习资源

| 资源 | 说明 |
|------|------|
| [CrewAI 官方文档](https://docs.crewai.com/) | 必读：Quickstart、Agents、Tasks、Crews、Flows |
| [CrewAI GitHub](https://github.com/crewAIInc/crewAI) | 官方仓库含 example 项目 |
| [AutoGen 官方文档](https://microsoft.github.io/autogen/) | 微软多 Agent 框架 |
| [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) | `multi_agent_collaboration_system.ipynb`、`research_team_autogen.ipynb`、`grocery_management_agents_system.ipynb` |

---

## 学习节奏建议

| 天数 | 完成任务 | 核心产出 |
|------|---------|---------|
| Day 1-2 | 任务 1：CrewAI 快速上手 | first_crew.py |
| Day 3-4 | 任务 2：角色分工与团队设计 | designed_crew.py + YAML 配置 |
| Day 5-6 | 任务 3：顺序 vs 并行执行 | execution_modes.py + 性能报告 |
| Day 7-8 | 任务 4：CrewAI Flow | crew_flow.py |
| Day 9-10 | 任务 5：AutoGen 入门 | autogen_demo.py |
| Day 11-14 | 任务 6：综合实战"内容创作团队" | content_team/ 完整项目 |

---

## 阶段 5 完成后的你应该能

- [ ] 用 CrewAI 创建多角色 Agent 团队
- [ ] 设计合理的 Agent 角色分工和工具分配
- [ ] 选择合适的执行模式（sequential / parallel / 混合）
- [ ] 用 Flow API 实现事件驱动的多 Crew 编排
- [ ] 了解 AutoGen 并能做基本使用
- [ ] 判断什么场景需要多 Agent、什么场景单 Agent 就够了
- [ ] 完成"智能内容创作团队"完整项目

**全部打勾后，进入阶段 6：生产化与可视化部署。**
