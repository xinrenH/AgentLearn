# Day2 任务计划（超详细执行版）

## 日期
- 2026-05-06

## 你今天要完成什么
1. 把用户、任务、日志 3 组接口跑通。
2. 学会最基础的参数校验（防止空值、非法状态）。
3. 学会用 Swagger (`/docs`) 验证接口。

---

## 开始前准备（5分钟）

在 PowerShell 执行：

```powershell
cd D:\AIAgent\AgentLearn\Demo1
.\.venv\Scripts\Activate.ps1
Copy-Item .env.dev .env -Force
$env:APP_ENV="dev"
```

启动服务：

```powershell
uvicorn app.main:app --reload
```

打开浏览器：
- `http://127.0.0.1:8000/health`
- `http://127.0.0.1:8000/docs`

通过标准：
- `/health` 返回 `status=ok`
- `/docs` 能打开

---

## Step 1：先确认路由是否接好（10分钟）

### 1.1 检查 `api/router.py`
文件：[api/router.py](D:/AIAgent/AgentLearn/Demo1/api/router.py)

目标：确认 3 个路由都 include 了。

应该有这3行：
- `include_router(user_router)`
- `include_router(task_router)`
- `include_router(log_router)`

### 1.2 检查 `app/main.py`
文件：[app/main.py](D:/AIAgent/AgentLearn/Demo1/app/main.py)

目标：确认主应用里有：
- `app.include_router(api_router, prefix=settings.api_prefix)`

通过标准：
- `/docs` 页面能看到 `users`、`tasks`、`logs` 三组标签

---

## Step 2：用户接口完善（30分钟）

文件：[api/routes/user.py](D:/AIAgent/AgentLearn/Demo1/api/routes/user.py)

把 `UserIn` 改成（重点：`name` 非空、长度 2-20）：

```python
from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


class UserIn(BaseModel):
    name: str = Field(..., min_length=2, max_length=20, description="用户名")


@router.post("")
def create_user(body: UserIn):
    return UserService.create_user(body.name)


@router.get("")
def list_users():
    return UserService.list_users()
```

Swagger 测试：
1. `POST /api/users`，body：`{"name":"Tom"}`
2. `GET /api/users`

通过标准：
- 创建成功返回用户对象
- 列表里能看到 `Tom`
- 传空字符串会报 422

---

## Step 3：任务接口完善（40分钟）

文件：[api/routes/task.py](D:/AIAgent/AgentLearn/Demo1/api/routes/task.py)

把代码改成下面（重点：状态枚举校验）：

```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Literal
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


class TaskIn(BaseModel):
    title: str = Field(..., min_length=2, max_length=50, description="任务标题")


class TaskStatusIn(BaseModel):
    status: Literal["todo", "in_progress", "done"]


@router.post("")
def create_task(body: TaskIn):
    return TaskService.create_task(body.title)


@router.get("")
def list_tasks():
    return TaskService.list_tasks()


@router.patch("/{task_id}/status")
def update_task_status(task_id: int, body: TaskStatusIn):
    updated = TaskService.update_status(task_id, body.status)
    if not updated:
        raise HTTPException(status_code=404, detail="task not found")
    return updated
```

Swagger 测试顺序：
1. `POST /api/tasks`，`{"title":"写Day2日志"}`
2. `GET /api/tasks`
3. `PATCH /api/tasks/1/status`，`{"status":"done"}`
4. 再测一次不存在 ID：`PATCH /api/tasks/999/status`

通过标准：
- 有效状态可更新
- 不存在任务返回 404
- 非法状态（如 `finished`）返回 422

---

## Step 4：日志接口完善（20分钟）

文件：[api/routes/log.py](D:/AIAgent/AgentLearn/Demo1/api/routes/log.py)

改成：

```python
from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.services.log_service import LogService

router = APIRouter(prefix="/logs", tags=["logs"])


class LogIn(BaseModel):
    content: str = Field(..., min_length=1, max_length=200, description="日志内容")


@router.post("")
def add_log(body: LogIn):
    return LogService.add_log(body.content)


@router.get("")
def list_logs():
    return LogService.list_logs()
```

Swagger 测试：
1. `POST /api/logs`，`{"content":"Day2接口测试通过"}`
2. `GET /api/logs`

通过标准：
- 能写入并查询
- 空内容报 422

---

## Step 5：统一响应格式（先做最简版，30分钟）

### 5.1 新建工具函数
文件：[core/response.py](D:/AIAgent/AgentLearn/Demo1/core/response.py)

```python
def ok(data=None, message="success"):
    return {"code": 0, "message": message, "data": data}


def fail(code: int, message: str, errors=None):
    return {"code": code, "message": message, "errors": errors}
```

### 5.2 在一个接口先试点
先改 `api/routes/user.py` 的两个返回：

```python
from core.response import ok

@router.post("")
def create_user(body: UserIn):
    return ok(UserService.create_user(body.name))

@router.get("")
def list_users():
    return ok(UserService.list_users())
```

通过标准：
- 接口返回结构变成 `code/message/data`

---

## Step 6：今天的最终验收（15分钟）

按这个顺序全部测一遍：
1. `GET /health`
2. `POST /api/users`
3. `GET /api/users`
4. `POST /api/tasks`
5. `PATCH /api/tasks/{id}/status`
6. `POST /api/logs`
7. `GET /api/logs`

如果全部通过，Day2 就完成。

---

## 你今天结束时要留下的产物
1. 代码改动（user/task/log 三个路由 + response 工具）
2. Swagger 测试截图（至少 3 张）
3. 更新工作日志：
   - 文件：[第1周工作日志-2026-04-27至2026-05-03.md](D:/AIAgent/AgentLearn/第1周工作日志-2026-04-27至2026-05-03.md)
   - 补 Day2 的“实际执行明细 + 验收结果”

---

## 常见报错快速排查
1. `ModuleNotFoundError`
- 看导入路径和文件名是否一致。

2. `ValidationError`
- 看 `.env` 或请求参数类型是否匹配。

3. `/docs` 打不开
- 检查 `uvicorn app.main:app --reload` 是否在 `Demo1` 目录执行。

4. 改了代码没生效
- 先停服务，再重启 `uvicorn`。

---

## Day3 预告
明天进入数据库：
1. 安装 `sqlalchemy` + `psycopg2-binary`
2. 建立数据库连接
3. 把内存仓储改成 PostgreSQL 持久化
