# Day1复习笔记

## 日期
- 2026-05-06

## 本次复习目的
- 回忆 Day1 到底做了什么。
- 把“为什么这样做”讲清楚，避免只会复制命令。
- 记录当前还不熟的点，后续反复看这一页即可。

## Day1核心内容（1句话）
- Day1 做的是：搭项目骨架 + 跑通服务 + 配置分层 + 三层结构（路由/服务/存储）定型。

## 本次你的关键提问与结论

1. 提问：`之前启动没这么复杂`
- 结论：你记得对。日常启动可以简化成一条命令。
- 最简启动：
```powershell
cd D:\AIAgent\AgentLearn\Demo1
.\start.ps1
```
- 说明：复杂步骤主要出现在“首次搭建”和“排错阶段”。

2. 提问：`GET / 返回 404`
- 结论：这是正常现象，不是程序崩了。
- 原因：项目里没有定义根路由 `/`。
- 正确检查地址：
  - `http://127.0.0.1:8000/health`
  - `http://127.0.0.1:8000/docs`

3. 提问：`/api/users 是空的`
- 结论：这是正常现象。
- 原因：当前是内存仓储，服务刚启动时数据为空；且重启后会清空。
- 验证方法：先 `POST /api/users` 创建用户，再 `GET /api/users` 查询。

## 本次暴露的“未完全理解点”

1. 启动流程和初始化流程的区别
- 初始化（首次）要做：创建 `.venv`、安装依赖、准备 `.env`。
- 日常启动只要做：激活环境或直接 `start.ps1`。

2. 404 和报错的区别
- 404（特定路径）通常是“没这个路由”。
- 程序报错通常会在控制台出现 Traceback。

3. 内存存储 vs 数据库存储
- 现在：数据在 `memory.py`，重启会丢。
- Day3：接 PostgreSQL 后才会持久化。

## Day1你现在必须记住的4个文件

1. [main.py](D:/AIAgent/AgentLearn/Demo1/app/main.py)
- 应用入口，挂载总路由和健康检查。

2. [config.py](D:/AIAgent/AgentLearn/Demo1/core/config.py)
- 配置分层（dev/test），读取环境变量。

3. [router.py](D:/AIAgent/AgentLearn/Demo1/api/router.py)
- 聚合 `users/tasks/logs` 路由。

4. [memory.py](D:/AIAgent/AgentLearn/Demo1/app/repositories/memory.py)
- 当前内存数据源，重启清空。

## 你的最小自测清单（2分钟）

1. 启动服务：`.\start.ps1`
2. 打开 `/health`：确认服务活着。
3. 打开 `/docs`：确认接口可调。
4. `POST /api/users` 创建 1 条数据。
5. `GET /api/users` 能查到刚创建的数据。

## 结论
- 你已经完成 Day1 的核心能力。
- 当前不是“不会做”，而是对“为什么会 404、为什么会空数据、为什么启动有时复杂”还在建立直觉。
- 这三个点已经厘清，Day2 可以继续推进。
