# 阶段0：Python 基础 — 学习任务说明文档

> **定位**：为 AI Agent 开发打地基。不要求精通 Python，但必须掌握后续写 Agent 时每天都要用的核心能力。
> **目标人群**：听说过 Python，可能写过 `print("hello world")`，但不能独立完成一个百行以上的小程序。
> **总时长**：每天 2 小时，约 4-6 周完成。
> **使用方式**：每个练习先看"教学示例"理解代码，再看"代码解析"搞清楚每一行是干什么的，最后自己动手做"实战练习"。

---

## 学习前必读：哪些 Python 知识是 Agent 开发真正用到的？

不要试图"系统学完 Python"。Agent 开发中真正高频使用的只有这些：

- `async/await` — 所有 Agent 框架底层都是异步的
- 类型注解 + Pydantic `BaseModel` — 定义 LLM 输入输出的结构
- 字典/JSON 操作 — LLM 的所有交互都是 JSON
- f-string 字符串拼接 — 构造 Prompt
- `try/except` 异常处理 — LLM 调用随时可能出错
- `pip` + `venv` — 管理项目依赖

---

## 学习任务 1：搭建开发环境 + 写出第一个程序

### 任务目标
在本地搭建 Python 开发环境，理解什么是"虚拟环境"，跑通第一个 Python 程序。

### 学习内容
- Python 安装与版本确认（需要 3.10+）
- 虚拟环境是什么、为什么需要它
- `pip install` 安装第三方包
- 写出第一行代码并运行

---

### 教学示例：第一个 Python 程序

创建一个文件 `hello.py`，写入以下代码：

```python
# hello.py — 第一个 Python 程序

def greet(name):
    """向指定的人打招呼"""
    return f"你好，{name}！欢迎来到 Python 的世界。"

# 当直接运行这个文件时执行以下代码
if __name__ == "__main__":
    # 调用函数并打印结果
    message = greet("小明")
    print(message)

    # 再试几个名字
    print(greet("小红"))
    print(greet("AI 学习者"))
```

### 代码解析

```python
def greet(name):                          # def = define，定义一个函数。greet 是函数名，(name) 是参数
    """向指定的人打招呼"""               # 三引号是文档字符串，描述函数的作用
    return f"你好，{name}！..."          # return 把结果返回给调用者。f"..." 是 f-string，{name} 会被替换成传入的实际值
```

```python
if __name__ == "__main__":               # 判断：这个文件是直接运行的，还是被 import 的？
    message = greet("小明")               # 调用函数，参数是 "小明"，返回值赋给变量 message
    print(message)                        # print() 把内容输出到终端
```

**关键概念**：
- `def` + `return` = 定义了一个"输入→输出"的转换器
- `f"{变量}"` = f-string，Python 最常用的字符串拼接方式（以后构造 Prompt 天天用）
- `if __name__ == "__main__"` = Python 程序的入口习惯，写不写都能跑，但建议养成习惯

---

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 1.1 | 安装 Python | 从 [python.org](https://python.org) 下载 3.11+，命令行输入 `python --version` 确认成功 |
| 1.2 | 创建项目目录 | 新建 `python-practice/` 文件夹，进入后创建虚拟环境：`python -m venv .venv` |
| 1.3 | 激活虚拟环境 | Windows: `.venv\Scripts\activate`；Mac/Linux: `source .venv/bin/activate` |
| 1.4 | 安装第一个包 | `pip install requests`，验证：`python -c "import requests; print('ok')"` |
| 1.5 | 写第一个程序 | 仿照教学示例，自己写一个 `hello.py`，修改 `greet()` 函数，让它返回不同风格的问候语 |

### 产出物
- 一个能运行的 `hello.py` 文件

### 验收标准
- [ ] 能在终端运行自己的 Python 代码
- [ ] 能用 `pip` 安装任意第三方库
- [ ] 知道虚拟环境的作用：隔离不同项目的依赖

---

## 学习任务 2：基本数据类型与运算

### 任务目标
掌握 Python 的核心数据类型，能完成简单的数据处理。

### 学习内容
- 数字（int, float）、字符串（str）、布尔（bool）
- 字符串格式化：f-string
- 类型转换：`str()`、`int()`、`float()`
- 基本运算：`+`、`-`、`*`、`/`、`%`、`//`

---

### 教学示例：计算器 + 温度转换 + Prompt 模板

```python
# basics.py — 数据类型与运算

def calculate(a, b, op):
    """根据运算符执行四则运算"""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:                         # 除以 0 会报错，先检查
            return "错误：除数不能为 0"
        return a / b
    else:
        return "错误：不支持的运算符"


def celsius_to_fahrenheit(celsius):
    """摄氏度 → 华氏度"""
    fahrenheit = celsius * 9 / 5 + 32
    return round(fahrenheit, 2)            # round() 保留两位小数


def fahrenheit_to_celsius(fahrenheit):
    """华氏度 → 摄氏度"""
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 2)


def make_prompt(topic, style):
    """生成一个 LLM 提示词模板"""
    return f"请用{style}的风格，写一段关于{topic}的介绍。字数不超过 200 字。"


# 测试代码
if __name__ == "__main__":
    print(calculate(10, 5, "+"))           # 输出：15
    print(calculate(10, 0, "/"))           # 输出：错误：除数不能为 0

    print(celsius_to_fahrenheit(36.5))     # 输出：97.7
    print(fahrenheit_to_celsius(100))      # 输出：37.78

    print(make_prompt("人工智能", "幽默")) # 输出：请用幽默的风格，写一段关于人工智能的介绍...
```

### 代码解析

```python
def calculate(a, b, op):
    if op == "+":                          # if/elif/else 是条件判断
        return a + b                       # 这里用了 return，函数立即结束，后面的代码不执行
    elif op == "-":                         # elif = else if，"否则如果"
        return a - b
    ...
    else:                                  # 所有条件都不满足时走这里
        return "错误：不支持的运算符"
```

```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32     # 数学公式直接写，Python 理解四则运算优先级
    return round(fahrenheit, 2)            # round(数字, 小数位数)
```

```python
def make_prompt(topic, style):
    return f"请用{style}的风格，写一段关于{topic}的介绍。"
    # f-string 中大括号 {} 里的变量会被替换成它的值
    # 这其实就是构造 Prompt 的最简单方式
```

**关键概念**：
- `if/elif/else` = 让程序根据条件走不同分支
- `round(x, 2)` = 保留两位小数
- f-string 是构造 Prompt 最基本的手段——后续阶段天天用

---

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 2.1 | 计算器 | 写函数 `calculate(a, b, op)`，支持 `+ - * /` 四种运算。除以 0 时返回 "除数不能为 0" |
| 2.2 | 温度转换器 | 写 `celsius_to_fahrenheit(c)` 和 `fahrenheit_to_celsius(f)`，输出保留两位小数 |
| 2.3 | 字符串模板 | 写函数 `make_prompt(topic, style)`，返回 `f"请用{style}的风格，写一段关于{topic}的介绍"` |

### 产出物
- 一个 `basics.py` 文件，包含上述 3 个函数

### 验收标准
- [ ] 能用 f-string 拼接字符串（这是以后构造 Prompt 的基本功）
- [ ] 能处理不同数据类型之间的转换

---

## 学习任务 3：列表、字典、集合

### 任务目标
理解 Python 三大容器的用法和区别。这是 Agent 开发中最常用的数据结构。

### 学习内容
- 列表（list）：增删改查、遍历、切片
- 字典（dict）：键值对、取值、设值、遍历
- 集合（set）：去重、交集、并集
- **列表推导式（list comprehension）** — 一行代码处理列表，高频使用

---

### 教学示例：三种容器的完整用法

```python
# containers.py — 列表、字典、集合

# ============================================================
# 一、列表（list）—— 有顺序的容器，用 [] 表示
# ============================================================

# 增删改查
tasks = ["写周报", "回邮件"]
tasks.append("开会")                       # ["写周报", "回邮件", "开会"]
first = tasks.pop(0)                       # 移除并返回第一个："写周报"
tasks[0] = "回紧急邮件"                    # 修改：["回紧急邮件", "开会"]
print(len(tasks))                          # 2（列表长度）

# 遍历
for task in tasks:                         # for...in... 是遍历列表最常用的写法
    print(f"待办：{task}")


# ============================================================
# 二、字典（dict）—— 键值对容器，用 {} 表示
# ============================================================
# 格式：{key: value, key: value, ...}
# 以后 LLM 的所有消息、API 的请求和响应，几乎全是这种结构！

# 翻译字典
translations = {
    "hello": "你好",
    "world": "世界",
    "python": "蟒蛇",
}

word = "hello"
if word in translations:                   # 用 in 检查 key 是否存在
    print(translations[word])              # 输出：你好
else:
    print("未收录")

# 增删改
translations["agent"] = "智能体"           # 添加
translations["python"] = "Python编程语言"  # 修改
del translations["world"]                  # 删除
print(translations.keys())                 # 所有 key：dict_keys(['hello', 'python', 'agent'])

# 遍历字典
for key, value in translations.items():    # .items() 同时拿到 key 和 value
    print(f"{key} → {value}")


# ============================================================
# 三、集合（set）—— 无序、不重复，用 {} 或 set() 表示
# ============================================================

# 去重
words = ["你好", "你好", "再见", "再见", "谢谢"]
unique_words = list(set(words))            # set() 去重，list() 转回列表
print(unique_words)                        # 结果顺序不固定，如 ['再见', '你好', '谢谢']

# 集合运算
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a & set_b)                       # 交集：{3, 4}
print(set_a | set_b)                       # 并集：{1, 2, 3, 4, 5, 6}


# ============================================================
# 四、列表推导式 —— 一行代码搞定循环+过滤+转换
# ============================================================
# 这是 Python 的标志性语法，后面处理 LLM 输出时天天用

numbers = [1, 5, 10, 15, 20, 25]

# 需求：把所有数字平方，只保留结果大于 100 的
result = [n * n for n in numbers if n * n > 100]
# 拆解：
#   n * n           → 对每个元素做什么操作（转换）
#   for n in numbers → 遍历哪个列表
#   if n * n > 100  → 什么条件才保留（过滤）
print(result)  # [225, 400, 625]

# 对比：不用列表推导式的等价写法
result2 = []
for n in numbers:
    squared = n * n
    if squared > 100:
        result2.append(squared)
# 上面 4 行 = 列表推导式 1 行
```

### 代码解析

**列表 vs 字典 vs 集合，什么时候用哪个？**

| 场景 | 用 | 原因 |
|------|-----|------|
| 存一组任务、一组消息 | 列表 `[]` | 有顺序，可以重复 |
| 存配置、存映射关系 | 字典 `{}` | 通过 key 快速查找 value |
| 去重、判断是否存在 | 集合 `set()` | 自动去重，查找极快 |

**LLM 开发中最常用的是字典**，因为：
- LLM 请求体是字典：`{"role": "user", "content": "你好"}`
- LLM 响应体是字典：`{"choices": [{"message": {"content": "你好！"}}]}`
- 所有配置是字典：`{"model": "gpt-4o", "temperature": 0.7}`

**列表推导式是高频语法**：
```python
# 从 LLM 响应中提取所有 tool_calls 的 name
tool_names = [tc.function.name for tc in response.choices[0].message.tool_calls]
```

---

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 3.1 | 任务管理器 | 用列表存储任务名，实现 `add_task(tasks, name)`、`remove_task(tasks, name)`、`list_tasks(tasks)` |
| 3.2 | 翻译字典 | 用字典存中英文映射，实现 `translate(word)`，未找到返回 `"未收录"` |
| 3.3 | 消息去重 | 给一个含重复元素的列表 `["你好","你好","再见"]`，用集合去重返回 |
| 3.4 | 列表推导式 | 一行代码：把一个数字列表所有元素平方，滤掉大于 100 的 |

### 产出物
- 一个 `containers.py` 文件，包含以上所有函数

### 验收标准
- [ ] 能熟练操作字典的增删改查和遍历
- [ ] 能写列表推导式
- [ ] 理解 JSON 其实就是"字符串形式的字典/列表"

---

## 学习任务 4：函数、作用域、装饰器入门

### 任务目标
深入理解函数——这是 Agent 框架中最基础的"积木块"。

### 学习内容
- 函数定义、参数、返回值、类型注解
- 默认参数、关键字参数、`*args`、`**kwargs`
- 作用域（local / global）
- **装饰器基础**：理解 `@xxx` 语法（Agent 中用 `@agent.tool` 注册工具函数）

---

### 教学示例：从普通函数到装饰器

```python
# functions.py — 函数进阶

# ============================================================
# 一、类型注解 —— 告诉别人（和 IDE）参数应该是什么类型
# ============================================================

# 没有类型注解（模糊）
def add(a, b):
    return a + b

# 有类型注解（清晰）
def add_typed(a: int, b: int) -> int:
    """
    参数：
        a: int  — 第一个加数，必须是整数
        b: int  — 第二个加数，必须是整数
    返回：
        int — 两数之和
    """
    return a + b


# ============================================================
# 二、参数的各种传法
# ============================================================

def build_request(url: str, method: str = "GET", **headers: str) -> dict:
    """
    构造一个 HTTP 请求的描述信息

    参数：
        url: 请求地址（必填）
        method: 请求方法，默认 "GET"
        **headers: 任意个键值对，作为请求头（可变关键字参数）

    返回：
        dict — 请求的完整描述
    """
    return {
        "url": url,
        "method": method,
        "headers": headers,    # headers 是一个字典，由 ** 自动收集
    }

# 调用示例
req = build_request(
    "https://api.openai.com/v1/chat/completions",
    method="POST",
    Authorization="Bearer sk-xxx",
    Content_Type="application/json",
)
print(req)
# 输出：{'url': 'https://api.openai.com/...', 'method': 'POST',
#        'headers': {'Authorization': 'Bearer sk-xxx', 'Content_Type': 'application/json'}}

# 参数规则：
#   url           → 位置参数（必填）
#   method="GET"  → 默认参数（可选，不传就用默认值）
#   **headers     → 把所有没被前面参数匹配的关键字参数，全收进一个字典


# ============================================================
# 三、装饰器 —— 给函数"套壳"，在不修改原函数的情况下增加功能
# ============================================================
# 这是理解 @agent.tool 的前提！

# 步骤 1：创建一个全局列表，用于存放所有"注册过的工具"
TOOLS = []


# 步骤 2：定义装饰器
def register_tool(func):
    """
    装饰器：把被装饰的函数自动加入 TOOLS 列表

    @register_tool          ← 在函数定义上写 @装饰器名
    def my_tool():          ← 这个函数就会被自动注册
        ...
    """
    TOOLS.append(func)                     # 把函数加入全局工具列表
    return func                            # 原样返回函数（不修改它）


# 步骤 3：使用装饰器注册工具
@register_tool
def search_web(query: str) -> str:
    """搜索网页"""
    return f"搜索结果：关于「{query}」的相关内容..."


@register_tool
def calculate(expression: str) -> float:
    """执行数学运算"""
    return eval(expression)                # eval() 把字符串当 Python 表达式执行


@register_tool
def get_time() -> str:
    """获取当前时间"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 步骤 4：从工具列表查找并调用
def call_tool(name: str, *args):
    """根据工具名找到函数并调用"""
    for tool in TOOLS:
        if tool.__name__ == name:          # __name__ 是函数的名字
            return tool(*args)             # 调用找到的函数
    return f"未找到工具：{name}"


# 测试
if __name__ == "__main__":
    print(f"已注册 {len(TOOLS)} 个工具：{[t.__name__ for t in TOOLS]}")
    # 输出：已注册 3 个工具：['search_web', 'calculate', 'get_time']

    print(call_tool("search_web", "Python教程"))
    # 输出：搜索结果：关于「Python教程」的相关内容...

    print(call_tool("calculate", "10 + 20 * 3"))
    # 输出：70

    print(call_tool("get_time"))
    # 输出：2026-05-07 15:30:00
```

### 代码解析

**类型注解不是强制的，但强烈建议写**：
```python
def foo(a: int, b: str) -> bool:   # 参数类型 → 返回类型
    ...
# Python 不会强制检查，但 IDE 会提示你，队友（和 3 个月后的你）会感谢你
```

**装饰器的本质**：
```python
@register_tool           # 这一行等价于：
def my_func():           # my_func = register_tool(my_func)
    ...
# 即：把函数作为参数传给装饰器，装饰器返回（可能修改过的）函数
```

**这和 Agent 框架的关系**：
```python
# PydanticAI 就是这么注册工具的：
@agent.tool                         # ← 装饰器！
async def get_weather(city: str):
    return f"{city}: 晴天"
# 跟上面 @register_tool 完全一样的原理！
```

---

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 4.1 | 参数组合 | 写函数 `build_request(url, method="GET", **headers)`，打印构造出的请求信息 |
| 4.2 | 类型注解 | 给任务 2-3 中写的所有函数加上完整的类型注解 |
| 4.3 | 模拟工具注册 | 仿照教学示例，写装饰器 `@register_tool`，注册 3 个自己的"工具函数" |
| 4.4 | 工具调用模拟 | 从 `TOOLS` 列表里根据函数名找到对应函数并调用它 |

### 产出物
- `functions.py` 包含以上实现

### 验收标准
- [ ] 能写出带类型注解的函数
- [ ] 理解 `**kwargs` 把额外的关键字参数收集成字典
- [ ] 理解装饰器的工作方式（这是理解 `@agent.tool` / `@tool` 的前提）

---

## 学习任务 5：文件读写与 JSON 处理

### 任务目标
能读写文件、处理 JSON。Agent 的配置、日志、数据存储都依赖文件 I/O。

### 学习内容
- `open()` 读文件
- `with` 语句自动管理资源
- `json.dumps()` / `json.loads()` — Python 对象 ↔ JSON 字符串
- `json.dump()` / `json.load()` — 直接读写 JSON 文件

---

### 教学示例：对话记录存储系统

```python
# file_handler.py — 文件读写与 JSON 处理

import json
import os
from datetime import datetime


# ============================================================
# 一、配置文件读写
# ============================================================

def load_config(filepath: str) -> dict:
    """从 JSON 文件加载配置。文件不存在则返回默认值。"""
    if not os.path.exists(filepath):       # 检查文件是否存在
        print(f"⚠ 配置文件 {filepath} 不存在，使用默认配置")
        return {"model": "gpt-4o-mini", "temperature": 0.7}

    with open(filepath, "r", encoding="utf-8") as f:
        #    ↑       ↑         ↑              ↑
        # with   文件名    "r"=只读    encoding 解决中文乱码
        config = json.load(f)              # json.load() 从文件对象读取并解析
    return config


def save_config(filepath: str, config: dict):
    """保存配置到 JSON 文件"""
    with open(filepath, "w", encoding="utf-8") as f:
        #                       ↑ "w"=写模式（会覆盖原有内容）
        json.dump(config, f, ensure_ascii=False, indent=2)
        #               ↑              ↑                ↑
        #        Python对象      不转义中文     缩进2格(好看)


# ============================================================
# 二、对话记录存储 — 最接近 Agent 实际使用场景
# ============================================================

class ChatHistory:
    """对话历史管理器 —— 存储和读取 LLM 对话记录"""

    def __init__(self, filepath: str):
        """
        初始化：指定存储文件路径，加载已有记录
        """
        self.filepath = filepath
        self.messages = self._load()        # 启动时加载已有消息

    def _load(self) -> list[dict]:
        """从文件加载消息列表"""
        if not os.path.exists(self.filepath):
            return []                       # 文件不存在，返回空列表
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save(self):
        """把当前消息列表保存到文件"""
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.messages, f, ensure_ascii=False, indent=2)

    def add(self, role: str, content: str):
        """
        添加一条消息
        role: "user" / "assistant" / "system"
        content: 消息内容
        """
        message = {
            "role": role,
            "content": content,
            "time": datetime.now().isoformat(),   # isoformat() 生成标准时间字符串
        }
        self.messages.append(message)
        self._save()                         # 每次添加自动保存

    def get_all(self) -> list[dict]:
        """获取所有消息"""
        return self.messages

    def get_last_n(self, n: int) -> list[dict]:
        """获取最近 n 条消息"""
        return self.messages[-n:]            # 负数索引：从倒数第 n 个到末尾

    def clear(self):
        """清空所有消息"""
        self.messages = []
        self._save()


# ============================================================
# 三、JSON 字符串 ↔ Python 对象的互相转换
# ============================================================

# Python 对象 → JSON 字符串
data = {"name": "张三", "age": 25, "skills": ["Python", "AI"]}
json_string = json.dumps(data, ensure_ascii=False, indent=2)
print(json_string)
# 输出：
# {
#   "name": "张三",
#   "age": 25,
#   "skills": ["Python", "AI"]
# }

# JSON 字符串 → Python 对象
json_string = '{"model": "gpt-4o", "messages": [{"role": "user", "content": "你好"}]}'
parsed = json.loads(json_string)           # json.loads() 注意有 s（string），从字符串解析
print(parsed["model"])                     # 输出：gpt-4o
print(parsed["messages"][0]["content"])    # 输出：你好
#       [字典]     [列表]   [字典]


# ============================================================
# 四、测试
# ============================================================

if __name__ == "__main__":
    # 测试配置读写
    config = load_config("config.json")
    config["temperature"] = 0.5
    save_config("config.json", config)

    # 测试对话历史
    history = ChatHistory("chat_history.json")
    history.add("system", "你是一个有用的助手")
    history.add("user", "今天天气怎么样？")
    history.add("assistant", "抱歉，我无法查询实时天气。")
    print(f"共有 {len(history.get_all())} 条消息")

    # 只取最近 2 条
    recent = history.get_last_n(2)
    for msg in recent:
        print(f"[{msg['role']}] {msg['content']}")
```

### 代码解析

**`json.load()` vs `json.loads()`，一字之差**：
```python
json.load(file_object)    # 从文件读  （没有 s）
json.loads(json_string)   # 从字符串读（有 s，s = string）
# dump/dumps 同理
```

**`with open(...) as f:` 为什么总这样写？**
```python
# 不好的写法（可能忘记关闭文件，导致数据丢失）
f = open("file.txt", "r")
data = f.read()
f.close()     # ← 容易忘！

# 好的写法（Python 自动帮你关闭文件）
with open("file.txt", "r") as f:
    data = f.read()
# 缩进结束后，Python 自动调用 f.close()，即使中间出错了也会关
```

**为什么这段代码和 Agent 开发紧密相关？**
```python
# 你以后调用 LLM API 的请求体就是这样构造的：
request_body = {
    "model": "gpt-4o",
    "messages": history.get_last_n(10),    # ← 从存储中读最近 10 条
    "temperature": 0.7,
}
# json.dumps(request_body) → 发送给 API
```

---

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 5.1 | 配置文件读写 | 创建 `config.json`，用 Python 读取并修改 `temperature` 字段后写回 |
| 5.2 | 对话记录存储 | 仿照教学示例，写一个 `ChatHistory` 类，支持添加消息、读取所有消息、读取最近 N 条 |
| 5.3 | 数据导出 | 读取 `[{"name":"张三","score":85},{"name":"李四","score":92}]`，导出为 CSV |

### 产出物
- `file_handler.py` 包含上述功能
- 一个真实的 `config.json` 和 `chat_history.json`

### 验收标准
- [ ] 能读写 JSON 文件来存取数据
- [ ] 能处理文件不存在的情况（`try/except`）
- [ ] 理解 JSON 结构就是"字典的字符串形式"

---

## 学习任务 6：异常处理

### 任务目标
写出"不会崩"的代码。Agent 调用 LLM 时网络中断、返回格式错误、Token 超限天天发生，异常处理是生死线。

### 学习内容
- `try/except/finally`
- 常见异常类型：`ValueError`、`KeyError`、`TypeError`、`FileNotFoundError`
- 自定义异常

---

### 教学示例：LLM API 调用重试封装

```python
# error_handling.py — 异常处理与重试

import random
import time
import json


# ============================================================
# 一、基础异常处理
# ============================================================

def safe_divide(a: float, b: float) -> str:
    """安全除法：除数为 0 时不崩溃"""
    try:
        result = a / b
        return f"{a} / {b} = {result}"
    except ZeroDivisionError:
        return "错误：除数不能为 0"


def safe_get(d: dict, key: str):
    """安全取字典值：key 不存在返回 None 而不报错"""
    try:
        return d[key]
    except KeyError:
        return None
    # 其实有更简单的写法：d.get(key)，但这里演示 try/except 的模式


# ============================================================
# 二、LLM 调用模拟 + 重试机制（重要！）
# ============================================================

class LLMError(Exception):
    """自定义异常：LLM 调用相关错误"""
    pass


def call_llm(prompt: str) -> str:
    """
    模拟 LLM API 调用 — 有 50% 概率失败。
    实际开发中，网络抖动、API 限流、超时都是家常便饭。
    """
    # 模拟随机失败（实际场景：网络断开 / 服务器 500 / 余额不足等）
    fail_type = random.choice(["success", "timeout", "rate_limit", "server_error"])

    if fail_type == "timeout":
        raise LLMError("请求超时：LLM 服务响应时间过长")
    elif fail_type == "rate_limit":
        raise LLMError("请求过于频繁：请稍后再试（429）")
    elif fail_type == "server_error":
        raise LLMError("服务器内部错误（500）")
    else:
        return f"回复：{prompt[:30]}..."


def call_llm_with_retry(prompt: str, max_retries: int = 3) -> str:
    """
    带重试机制的 LLM 调用

    策略：
    - 超时、服务器错误 → 等一等再重试（可能是临时故障）
    - 限流 → 等久一点再重试（避免被封）
    - 重试 max_retries 次后仍失败 → 放弃，返回降级回复
    """
    for attempt in range(1, max_retries + 1):
        try:
            # 尝试调用
            result = call_llm(prompt)
            return result                          # 成功，直接返回

        except LLMError as e:
            error_msg = str(e)
            print(f"  [尝试 {attempt}/{max_retries}] 失败：{error_msg}")

            if attempt == max_retries:
                # 最后一次也失败了 → 放弃，走降级逻辑
                print(f"  ⚠ 已达最大重试次数，触发降级")
                return "抱歉，AI 服务暂时不可用，请稍后再试。"

            # 不是最后一次 → 等一会儿再重试
            if "限流" in error_msg or "429" in error_msg:
                wait = 3                           # 限流等 3 秒
            else:
                wait = 1                           # 其他错误等 1 秒
            print(f"  ⏳ 等待 {wait} 秒后重试...")
            time.sleep(wait)

    # 理论上走不到这里，但加上防止漏掉
    return "未知错误"


# ============================================================
# 三、JSON 解析保护
# ============================================================

def safe_parse_json(text: str) -> dict:
    """
    安全的 JSON 解析：格式错误时返回空字典并记录日志。
    LLM 输出的 JSON 不总是格式正确的！
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        # 记录错误日志（实际项目中用 logging 模块）
        print(f"[ERROR] JSON 解析失败：{e}")
        print(f"[ERROR] 原始文本：{text[:200]}")
        return {}                                # 返回空字典，不崩溃


# ============================================================
# 四、测试
# ============================================================

if __name__ == "__main__":
    # 测试安全操作
    print(safe_divide(10, 0))                    # 错误：除数不能为 0

    # 测试重试机制（多跑几次，观察不同失败场景的处理）
    for i in range(3):
        print(f"\n--- 第 {i+1} 次调用 ---")
        result = call_llm_with_retry("介绍一下 Python")
        print(f"最终结果：{result}")

    # 测试 JSON 保护
    print(safe_parse_json('{"valid": "json"}'))  # {'valid': 'json'}
    print(safe_parse_json('这不是JSON'))           # {}（不崩溃）
```

### 代码解析

**`try/except` 的核心思想**：
```python
try:
    # 可能出错的代码
    result = risky_operation()
except 特定异常类型 as e:
    # 出错后的补救措施
    handle_error(e)
# 程序继续运行，不会崩溃
```

**Agent 开发中最重要的模式：重试 + 降级**
```
尝试调 LLM → 网络超时 → 等 1 秒再试
              → 又失败 → 等 2 秒再试
              → 三次都失败 → 返回降级回复："服务暂时不可用"
```
这就是生产级 Agent 和玩具 Demo 之间的核心区别。

**实际 Agent 开发中的异常场景**：

| 异常 | 原因 | 处理策略 |
|------|------|---------|
| 网络超时 | API 服务器卡了 | 重试 3 次，间隔递增 |
| 429 限流 | 请求太快太多 | 等更久再重试（3-5 秒）|
| 401 未授权 | API Key 过期/错了 | 立即失败，提示用户检查 |
| JSON 解析失败 | LLM 输出了非标准 JSON | 抛出错误信息让 LLM 重新生成 |
| Token 超出限制 | 对话太长 | 截断历史消息后重试 |

---

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 6.1 | 安全除法 | 写 `safe_divide(a, b)`，b=0 时返回友好提示 |
| 6.2 | 安全字典取值 | 写 `safe_get(d, key)`，key 不存在返回 None |
| 6.3 | LLM 调用 + 重试 | 仿照教学示例，实现模拟 LLM 调用的重试逻辑，最多重试 3 次 |
| 6.4 | JSON 解析保护 | 写 `safe_parse_json(text)`，解析失败返回空字典并打印错误信息 |

### 产出物
- `error_handling.py` 包含以上函数

### 验收标准
- [ ] 能写出带重试机制的代码
- [ ] 能在异常时记录有用的错误信息
- [ ] 程序不会因为未处理的异常而崩溃

---

## 学习任务 7：异步编程 async/await

### 任务目标
这是从"会 Python"到"能写 Agent"的**最关键一步**。所有 Agent 框架底层都是异步的。

### 学习内容
- 同步 vs 异步的区别（I/O 密集型 vs CPU 密集型）
- `async def` / `await`
- `asyncio.run()` 启动异步程序
- `asyncio.sleep()` vs `time.sleep()`
- `asyncio.gather()` 并发执行多个任务

---

### 教学示例：从同步到异步的完整对比

```python
# async_demo.py — 异步编程

import asyncio
import time
import random


# ============================================================
# 一、同步 vs 异步的直观对比
# ============================================================

# 同步版本 — 一个做完才做下一个（像排队买票，只有一个窗口）
def sync_demo():
    print("[同步] 开始...")
    start = time.time()

    time.sleep(1)            # 假装在处理任务（等 1 秒）
    print("[同步] 任务 A 完成")
    time.sleep(1)
    print("[同步] 任务 B 完成")
    time.sleep(1)
    print("[同步] 任务 C 完成")

    elapsed = time.time() - start
    print(f"[同步] 总耗时：{elapsed:.1f} 秒")
    # 输出：总耗时：3.0 秒


# 异步版本 — 并发执行（像开了 3 个窗口同时排 3 条队）
async def task(name: str, delay: float):
    """一个异步任务：等待 delay 秒后完成"""
    await asyncio.sleep(delay)    # ← 关键：await 让出控制权，其他任务可以同时跑
    print(f"[异步] 任务 {name} 完成")
    return f"结果-{name}"


# 关键对比：asyncio.sleep() vs time.sleep()
#   time.sleep(1)     → 阻塞整个线程，期间什么都干不了
#   await asyncio.sleep(1) → 暂停当前协程，允许其他协程继续运行


async def async_demo():
    print("[异步] 开始...")
    start = time.time()

    # 并发执行 3 个任务
    results = await asyncio.gather(
        task("A", 1.0),
        task("B", 1.0),
        task("C", 1.0),
    )
    # asyncio.gather() 同时启动所有任务，等全部完成
    # 3 个各等 1 秒的任务，并发执行只需要 ~1 秒！

    elapsed = time.time() - start
    print(f"[异步] 总耗时：{elapsed:.1f} 秒")
    print(f"[异步] 所有结果：{results}")
    # 输出：总耗时：1.0 秒（而不是 3 秒！）


# ============================================================
# 二、模拟并发 LLM 调用
# ============================================================

async def call_llm_async(prompt: str, model: str = "gpt-4o-mini") -> str:
    """
    模拟异步 LLM 调用。
    实际开发中，这里会用 httpx 发送 HTTP 请求。
    """
    delay = random.uniform(0.3, 0.8)          # 模拟不同的响应时间
    await asyncio.sleep(delay)
    return f"[{model}] 回复：{prompt[:15]}...（耗时 {delay:.2f}s）"


async def demo_parallel_llm():
    """并发调用 3 个 LLM 请求"""
    print("[并发 LLM] 同时发送 3 个请求...")
    start = time.time()

    # 同时发起 3 个不同的 LLM 请求
    results = await asyncio.gather(
        call_llm_async("北京天气怎么样？"),
        call_llm_async("上海天气怎么样？"),
        call_llm_async("广州天气怎么样？"),
    )

    elapsed = time.time() - start
    print(f"[并发 LLM] 总耗时：{elapsed:.2f} 秒")
    for r in results:
        print(f"  {r}")


# ============================================================
# 三、启动异步程序
# ============================================================

# 方法 1：直接用 asyncio.run()（最常用）
# asyncio.run(async_demo())

# 方法 2：在已有的异步函数中 await
# await async_demo()

# 方法 3：Jupyter Notebook 中可以直接 await
# await async_demo()

if __name__ == "__main__":
    print("=" * 50)
    sync_demo()

    print("\n" + "=" * 50)
    asyncio.run(async_demo())         # ← 启动异步程序的入口

    print("\n" + "=" * 50)
    asyncio.run(demo_parallel_llm())
```

### 代码解析

**同步代码 vs 异步代码的写法区别**：
```python
# 同步
def my_func():            # def
    result = do_something()  # 直接调用，阻塞等待
    return result

# 异步
async def my_func():      # async def
    result = await do_something()  # await 调用，不阻塞
    return result
```

**`await` 到底在等什么？在等 I/O 操作完成**：
```python
# 这些操作都是 I/O 密集型（大部分时间在等网络/磁盘响应）：
await httpx_client.get(url)            # 等 HTTP 响应
await asyncio.sleep(1)                 # 等时间
await openai_client.chat.complete(...) # 等 LLM 返回
await db.execute(query)                # 等数据库返回

# 这些是 CPU 密集型（一直在计算），不适合用异步：
big_list.sort()                        # 纯计算
image_processing(data)                 # 纯计算
```

**为什么 Agent 框架都用异步？**
```
场景：Agent 需要同时调用 LLM + 搜索工具 + 数据库查询

同步方式（排队）：
  LLM(3秒) → 搜索(2秒) → 数据库(1秒) = 总共 6 秒

异步方式（并发）：
  LLM(3秒) ┐
  搜索(2秒) ├─ 同时进行 → 总共 3 秒
  数据库(1秒)┘
```

**`asyncio.gather()` 的用法**：
```python
# 同时启动 N 个异步任务，等全部完成后返回结果列表
results = await asyncio.gather(
    task1(),
    task2(),
    task3(),
)
# results = [result1, result2, result3]
```

---

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 7.1 | 理解异步 | 写同步版本和异步版本各一个，对比总耗时。3 个任务各等 1 秒，同步 3 秒 vs 异步 1 秒 |
| 7.2 | 并发下载模拟 | 写 5 个异步函数，每个随机等 0.1~1 秒。用 `asyncio.gather` 并发执行，观察最终耗时 |
| 7.3 | 模拟 LLM 调用 | 写 `async def call_llm_async(prompt: str) -> str`，内部 `await asyncio.sleep(0.5)` 模拟延迟 |
| 7.4 | 并发调用 LLM | 同时发起 3 个不同 prompt 的 LLM 请求，用 `asyncio.gather` 收集结果 |

### 产出物
- `async_demo.py` 包含以上实现

### 验收标准
- [ ] 能写出 `async def` 函数并在其中使用 `await`
- [ ] 能用 `asyncio.gather` 并发执行多个异步任务
- [ ] 理解为什么异步比同步快：等待时让出控制权给其他任务

---

## 学习任务 8：类型注解与 Pydantic 模型

### 任务目标
掌握类型注解和 Pydantic `BaseModel`——这是 Agent 开发中最最重要的 Python 技能，没有之一。

### 学习内容
- 完整类型注解：`list[str]`、`dict[str, Any]`、`Optional[str]`、`Union[str, int]`
- **Pydantic `BaseModel`**：定义数据模型、自动校验、序列化
- Pydantic 环境变量配置：`BaseSettings`（管理 API Key）
- `model_dump()` / `model_dump_json()` — 模型转字典/JSON

---

### 教学示例：从类型注解到 Pydantic 模型

```python
# pydantic_demo.py — 类型注解与 Pydantic

# 先安装：pip install pydantic pydantic-settings

from typing import Any, Optional, Literal
from pydantic import BaseModel, Field, ValidationError
from pydantic_settings import BaseSettings
import json


# ============================================================
# 一、类型注解基础
# ============================================================

# 变量注解（Python 3.10+ 推荐语法）
name: str = "张三"
age: int = 25
scores: list[float] = [85.5, 92.0, 78.5]
config: dict[str, Any] = {"model": "gpt-4o", "temperature": 0.7}
#        ↑    ↑   ↑
#       key的 value的
#       类型  类型（Any=任意类型）

# 函数注解
def chat(
    messages: list[dict[str, str]],       # 字典列表：LLM 的消息格式
    model: str = "gpt-4o-mini",
    temperature: Optional[float] = None,   # Optional[X] = X 或 None
    stream: bool = False,
) -> dict[str, Any]:                      # 返回值类型
    ...


# ============================================================
# 二、Pydantic BaseModel — 数据模型 + 自动校验
# ============================================================

# 示例 1：用户模型
class User(BaseModel):
    """用户数据模型"""
    name: str                              # 必填，必须是字符串
    age: int = Field(ge=0, le=150)         # 0~150 之间
    email: str
    tags: list[str] = []                   # 有默认值，可选


# 正常数据 — 自动通过
user = User(name="张三", age=25, email="zhangsan@example.com")
print(user.name)                           # 张三
print(user.model_dump())                   # {'name': '张三', 'age': 25, 'email': '...', 'tags': []}

# 错误数据 — 自动报错！
try:
    bad_user = User(name="李四", age=999, email="xxx")
except ValidationError as e:
    print(f"校验失败：{e}")
    # 输出：age 超出范围；email 格式不对


# 示例 2：LLM 响应模型（重要！）
class LLMResponse(BaseModel):
    """LLM 结构化响应的标准格式"""
    answer: str                            # 主要回答
    confidence: float = Field(ge=0, le=1)  # 信心分数 0~1
    sources: list[str]                     # 引用的来源列表
    follow_up_questions: list[str] = []    # 建议的后续问题

    @property
    def is_confident(self) -> bool:
        """判断回答是否足够有信心"""
        return self.confidence >= 0.7


# 从 JSON 字符串自动解析并校验
llm_raw_output = '''
{
    "answer": "Python 是一种高级编程语言，由 Guido van Rossum 于 1991 年发布。",
    "confidence": 0.95,
    "sources": ["Python 官方文档", "Wikipedia"],
    "follow_up_questions": ["Python 的主要应用领域有哪些？"]
}
'''

response = LLMResponse.model_validate_json(llm_raw_output)
# model_validate_json() 做了三件事：
#   1. 解析 JSON 字符串
#   2. 校验每个字段的类型和约束
#   3. 创建 LLMResponse 对象

print(f"回答：{response.answer}")
print(f"信心：{response.confidence}")
print(f"足够自信？{response.is_confident}")  # True

# 转回字典（构造 API 请求体时常用）
response_dict = response.model_dump()
print(json.dumps(response_dict, ensure_ascii=False, indent=2))


# 示例 3：嵌套模型（更接近真实场景）
class ToolCall(BaseModel):
    """一次工具调用"""
    tool_name: str
    arguments: dict[str, Any]
    result: Optional[str] = None


class AgentStep(BaseModel):
    """Agent 的一个执行步骤"""
    step_number: int
    thought: str                           # Agent 的"思考"
    tool_call: Optional[ToolCall] = None   # 可选：这步调用了什么工具
    observation: Optional[str] = None      # 可选：观察到了什么结果


# 完整的 Agent 执行轨迹
agent_trace_json = '''
{
    "step_number": 1,
    "thought": "用户想查天气，我需要调用 get_weather 工具",
    "tool_call": {
        "tool_name": "get_weather",
        "arguments": {"city": "北京"},
        "result": "北京：25°C，晴"
    },
    "observation": "成功获取了北京的天气信息"
}
'''
step = AgentStep.model_validate_json(agent_trace_json)
print(step.thought)                        # 用户想查天气...


# ============================================================
# 三、BaseSettings — 从 .env 读配置（管理 API Key）
# ============================================================

class Settings(BaseSettings):
    """应用配置模型 — 自动从 .env 文件和环境变量读取"""
    openai_api_key: str                    # 必填：从 .env 的 OPENAI_API_KEY 读
    model_name: str = "gpt-4o-mini"        # 有默认值，可选
    temperature: float = 0.7
    max_retries: int = 3

    # 这行告诉 Pydantic 从 .env 文件加载
    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


# 使用（前提：项目根目录有 .env 文件，内容为 OPENAI_API_KEY=sk-xxx）
# settings = Settings()                    # 自动从 .env 读取
# print(settings.model_name)               # gpt-4o-mini
# print(settings.openai_api_key[:10])      # sk-...（前 10 位）
```

### 代码解析

**为什么 Agent 框架都选 Pydantic？**

```python
# 没有 Pydantic（手动处理）：
raw = '{"answer": "xxx", "confidence": 0.9}'
data = json.loads(raw)
if not isinstance(data["answer"], str):     # 手动检查类型
    raise TypeError(...)
if not (0 <= data["confidence"] <= 1):      # 手动检查范围
    raise ValueError(...)
# ... 每个字段都要写一堆校验代码

# 用 Pydantic（自动处理）：
response = LLMResponse.model_validate_json(raw)
# 一行搞定！类型不对？范围超了？自动抛异常并告诉你哪里错了
```

**`model_dump()` — 模型转字典**：
```python
# 以后你会经常这样写：
request_body = {
    "model": settings.model_name,
    "messages": messages,
    "temperature": settings.temperature,
    "response_format": {"type": "json_object"},
}
# 这就是发送给 LLM API 的请求体
```

**`Optional[X]` = `X | None`**：
```python
def foo(value: Optional[str] = None):
    # value 可以是 str 或者 None
    # 等价于 def foo(value: str | None = None)
```

---

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 8.1 | 类型注解 | 给之前写的所有函数加上完整的类型注解 |
| 8.2 | 第一个 Pydantic 模型 | 定义 `User` 模型（name, age, email），传入错误数据看 Pydantic 报错信息 |
| 8.3 | LLM 响应模型 | 仿照教学示例，定义 `LLMResponse`，从 JSON 字符串使用 `model_validate_json()` 解析 |
| 8.4 | 环境配置 | 用 `BaseSettings` 定义配置类，从 `.env` 读取 `OPENAI_API_KEY` 等 |

### 产出物
- `pydantic_demo.py` 包含以上模型定义

### 验收标准
- [ ] 能定义 Pydantic `BaseModel` 并自动校验
- [ ] 能从 JSON 字符串自动解析成 Python 对象（`model_validate_json()`）
- [ ] 能用 `BaseSettings` 管理配置（API Key 等）
- [ ] 理解 `model_dump()` 把模型转成字典

---

## 学习任务 9：HTTP 请求与 API 调用

### 任务目标
能用 Python 调任意 HTTP API。LLM 就是通过 HTTP API 调用的。

### 学习内容
- `httpx` 库（异步）发送 GET / POST 请求
- HTTP 状态码：200 / 400 / 401 / 429 / 500
- Bearer Token 鉴权（所有 LLM API 都用这个）

---

### 教学示例：LLM API 调用封装

```python
# api_client.py — HTTP 请求与 LLM API 调用

import asyncio
import httpx
import json
import os
from dotenv import load_dotenv

load_dotenv()  # 加载 .env 文件


# ============================================================
# 一、基础 HTTP 调用（公开 API）
# ============================================================

async def call_public_api():
    """调用 GitHub 公开 API（不需要鉴权）"""
    async with httpx.AsyncClient() as client:
        #                ↑ 创建异步 HTTP 客户端（用完自动关闭）
        response = await client.get("https://api.github.com")
        #              ↑      ↑    ↑
        #           客户端   GET   URL

        print(f"状态码：{response.status_code}")
        # 200 = 成功，404 = 不存在，500 = 服务器错误

        print(f"响应头：{dict(response.headers)}")
        # 响应头里有很多有用信息：Content-Type, Rate-Limit 等

        # 把响应体解析为 JSON
        data = response.json()
        # response.json() 等价于 json.loads(response.text)
        print(f"GitHub API 当前用户速率限制 URL：{data.get('current_user_url')}")


# ============================================================
# 二、LLM API 调用（需要 API Key）
# ============================================================

async def chat_completion(
    messages: list[dict],
    api_key: str | None = None,
    model: str = "gpt-4o-mini",
    temperature: float = 0.7,
    max_retries: int = 3,
) -> dict:
    """
    调用 OpenAI Chat Completions API

    参数：
        messages: 消息列表 [{"role": "user", "content": "..."}, ...]
        api_key: OpenAI API Key（不传则从环境变量读取）
        model: 模型名称
        temperature: 采样温度
        max_retries: 最大重试次数

    返回：
        dict — API 的 JSON 响应
    """
    api_key = api_key or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("未设置 OPENAI_API_KEY，请在 .env 文件中配置")

    url = "https://api.openai.com/v1/chat/completions"

    # 请求头——Bearer Token 鉴权
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    # Bearer Token 是最常见的 API 鉴权方式：
    #   服务端拿到你的 Token，验证身份后返回数据
    #   相当于"出示你的门禁卡"

    # 请求体
    body = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    # 带重试的请求
    async with httpx.AsyncClient(timeout=30.0) as client:
        #                            ↑ 30 秒超时
        for attempt in range(1, max_retries + 1):
            try:
                response = await client.post(url, json=body, headers=headers)

                # 根据状态码做不同处理
                if response.status_code == 200:
                    return response.json()                # 成功

                elif response.status_code == 401:
                    raise Exception("API Key 无效，请检查 .env 中的 OPENAI_API_KEY")

                elif response.status_code == 429:
                    print(f"  被限流，等待 3 秒后重试...（第 {attempt} 次）")
                    await asyncio.sleep(3)
                    continue                              # 重试

                elif response.status_code >= 500:
                    print(f"  服务器错误 {response.status_code}，等待 2 秒后重试...")
                    await asyncio.sleep(2)
                    continue                              # 重试

                else:
                    error = response.json()
                    raise Exception(f"API 错误：{error}")

            except httpx.TimeoutException:
                print(f"  请求超时，等待 2 秒后重试...（第 {attempt} 次）")
                await asyncio.sleep(2)
                continue

    raise Exception(f"调用失败，已重试 {max_retries} 次")


# ============================================================
# 三、测试
# ============================================================

async def main():
    # 测试公开 API
    print("--- 测试公开 API ---")
    await call_public_api()

    # 测试 LLM API（需要有 API Key）
    print("\n--- 测试 LLM API ---")
    messages = [
        {"role": "system", "content": "你是一个简洁的助手，回答不超过 20 个字。"},
        {"role": "user", "content": "什么是 Python？"},
    ]

    try:
        result = await chat_completion(messages)
        reply = result["choices"][0]["message"]["content"]
        usage = result["usage"]
        print(f"回复：{reply}")
        print(f"消耗：输入 {usage['prompt_tokens']} tokens + 输出 {usage['completion_tokens']} tokens")
    except Exception as e:
        print(f"调用失败：{e}")


if __name__ == "__main__":
    asyncio.run(main())
```

### 代码解析

**HTTP 请求的核心要素**：
```python
# 一个 HTTP 请求包含三个部分：
#   1. 方法：GET(读) / POST(写) / PUT(改) / DELETE(删)
#   2. URL：请求的地址
#   3. Header + Body：附带的信息

# GET 请求（获取数据，没有 body）
response = await client.get("https://api.example.com/data")

# POST 请求（提交数据，有 body）
response = await client.post(
    "https://api.example.com/submit",
    json={"key": "value"},         # ← 请求体
    headers={"Authorization": "Bearer xxx"}  # ← 请求头
)
```

**Bearer Token 鉴权**：
```python
headers = {"Authorization": f"Bearer {api_key}"}
# 所有主流 LLM API（OpenAI、Anthropic、Google 等）都用这种方式
# Authorization 头 = "Bearer " + 你的 API Key
```

**`async with httpx.AsyncClient()` 为什么这样写？**
```python
# httpx.AsyncClient 内部维护了连接池，复用 TCP 连接
# 用 async with 确保：a) 用完自动关闭  b) 出错也会关闭
# 不要每次都创建新 client，一个 client 复用多次请求
```

---

### 实战练习

| # | 练习 | 具体要求 |
|---|------|---------|
| 9.1 | 调用公开 API | 用 `httpx` 异步调用 `https://api.github.com`，打印状态码和部分响应 |
| 9.2 | LLM API 封装 | 仿照教学示例，实现 `chat_completion()` 函数（需要真实 API Key） |
| 9.3 | 错误处理 | 给 `chat_completion` 加上：401 提示 Key 无效、429 等待重试、500 重试 3 次 |
| 9.4 | 流式响应 | `stream=True` 后逐 chunk 打印 `delta.content` |

### 产出物
- `api_client.py` 包含 LLM API 调用封装

### 验收标准
- [ ] 能用 `httpx.AsyncClient` 发送异步 POST 请求
- [ ] 能根据 HTTP 状态码做不同的错误处理
- [ ] 理解 Bearer Token 鉴权方式
- [ ] （有 API Key 时）能获得 LLM 的真实回复

---

## 学习任务 10：综合实战 — 个人知识助手 CLI

### 任务目标
把前面学到的所有技能组装成一个**完整的命令行工具**。这是阶段 0 的"毕业设计"。

### 功能需求

```
个人知识助手 CLI
================
1. 添加笔记（标题 + 内容，保存到 JSON）
2. 搜索笔记（按关键词在标题和内容中匹配）
3. 列出所有笔记
4. 删除笔记（按标题）
5. AI 总结（把当前所有笔记摘要发给 LLM，返回一句话总结）
0. 退出
```

---

### 教学示例：核心代码骨架

```python
# notes_cli.py — 个人知识助手 CLI

import asyncio
import json
import os
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import httpx

load_dotenv()

# ============================================================
# 数据模型
# ============================================================

class Note(BaseModel):
    """笔记模型"""
    title: str = Field(min_length=1, description="笔记标题")
    content: str = Field(min_length=1, description="笔记内容")
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())


# ============================================================
# 数据存储
# ============================================================

class NoteStore:
    """笔记存储（JSON 文件持久化）"""

    def __init__(self, filepath: str = "notes.json"):
        self.filepath = filepath
        self.notes: list[Note] = self._load()

    def _load(self) -> list[Note]:
        """从文件加载笔记"""
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Note(**item) for item in data]
            #    ↑ 列表推导式 + Pydantic 解析：每一条 JSON 数据 → Note 对象

    def _save(self):
        """保存笔记到文件"""
        data = [note.model_dump() for note in self.notes]
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add(self, title: str, content: str):
        """添加笔记"""
        note = Note(title=title, content=content)
        self.notes.append(note)
        self._save()
        print(f"✅ 已添加笔记：{title}")

    def search(self, keyword: str) -> list[Note]:
        """搜索笔记（标题或内容包含关键词）"""
        keyword_lower = keyword.lower()
        return [
            note for note in self.notes
            if keyword_lower in note.title.lower()
            or keyword_lower in note.content.lower()
        ]

    def list_all(self):
        """列出所有笔记"""
        if not self.notes:
            print("📭 暂无笔记")
            return
        for i, note in enumerate(self.notes, 1):
            print(f"\n--- {i}. {note.title} ---")
            print(f"    {note.content[:100]}{'...' if len(note.content) > 100 else ''}")
            print(f"    [{note.created_at}]")

    def delete(self, title: str) -> bool:
        """按标题删除笔记"""
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                self._save()
                print(f"🗑 已删除笔记：{title}")
                return True
        print(f"❌ 未找到笔记：{title}")
        return False


# ============================================================
# AI 总结（调用 LLM）
# ============================================================

async def ai_summarize(notes: list[Note]) -> str:
    """调用 LLM 对所有笔记做一句话总结"""
    if not notes:
        return "暂无笔记可总结。"

    # 构造所有笔记的摘要
    notes_text = "\n".join(
        f"- {note.title}: {note.content[:50]}"
        for note in notes
    )

    prompt = f"以下是我的笔记列表，请用一句话总结这些笔记的主题和内容：\n\n{notes_text}"

    messages = [{"role": "user", "content": prompt}]

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "⚠ 未配置 OPENAI_API_KEY，跳过 AI 总结"

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                "https://api.openai.com/v1/chat/completions",
                json={
                    "model": "gpt-4o-mini",
                    "messages": messages,
                    "temperature": 0.7,
                },
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
            )
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                return f"⚠ AI 总结失败：HTTP {response.status_code}"
    except Exception as e:
        return f"⚠ AI 总结异常：{e}"


# ============================================================
# CLI 交互循环
# ============================================================

async def main():
    store = NoteStore()

    print("=" * 50)
    print("      个人知识助手 CLI")
    print("=" * 50)

    while True:
        print("\n" + "-" * 50)
        print("1. 添加笔记   2. 搜索笔记   3. 列出所有")
        print("4. 删除笔记   5. AI 总结    0. 退出")
        print("-" * 50)

        choice = input("请选择：").strip()

        try:
            if choice == "1":
                title = input("标题：").strip()
                content = input("内容：").strip()
                if title and content:
                    store.add(title, content)
                else:
                    print("❌ 标题和内容不能为空")

            elif choice == "2":
                keyword = input("搜索关键词：").strip()
                results = store.search(keyword)
                if results:
                    print(f"\n找到 {len(results)} 条结果：")
                    for note in results:
                        print(f"  📝 {note.title}: {note.content[:80]}...")
                else:
                    print(f"🔍 未找到包含「{keyword}」的笔记")

            elif choice == "3":
                store.list_all()

            elif choice == "4":
                title = input("要删除的笔记标题：").strip()
                store.delete(title)

            elif choice == "5":
                print("🤖 正在调用 AI 进行总结...")
                summary = await ai_summarize(store.notes)
                print(f"\n📊 AI 总结：{summary}")

            elif choice == "0":
                print("👋 再见！")
                break

            else:
                print("❌ 无效选项，请输入 0-5")

        except Exception as e:
            print(f"❌ 出错了：{e}")
            print("   别担心，程序还在运行。继续操作即可。")


if __name__ == "__main__":
    asyncio.run(main())
```

### 代码解析

**这个综合项目用到了前面学到的几乎所有技能**：

| 技能 | 在项目中的使用 |
|------|---------------|
| f-string | 构造菜单、构造 LLM prompt |
| 列表/字典 | 笔记存储、LLM 请求体 |
| 列表推导式 | `[Note(**item) for item in data]` |
| 类型注解 | 所有函数都有完整注解 |
| 装饰器原理 | Pydantic `Field()` 本质也是装饰器 |
| 文件 + JSON | `NoteStore` 的读写持久化 |
| 异常处理 | `try/except` 包裹整个菜单循环 |
| async/await | `main()` 是 async，`ai_summarize()` 是 async |
| Pydantic | `Note` 模型定义和校验 |
| httpx | `ai_summarize()` 中调用 LLM API |

**这就是一个"微缩版 Agent"**：
```
用户输入 → 你的代码处理 → 需要 LLM 帮助时调 API → 把结果展示给用户
```
和后续阶段要写的 Agent 原理完全相同，只是工具更多、流程更复杂。

---

### 实战练习

根据上面的教学示例，从头实现完整的"个人知识助手 CLI"。可以完全自己写，也可以基于示例修改扩展。

**扩展挑战（选做）**：
- 添加笔记分类功能（工作/学习/生活）
- 支持按时间范围筛选笔记
- 导出笔记为 Markdown 文件
- AI 总结时指定风格（简洁/详细/幽默）

### 技术要求
- 用 `asyncio` 实现异步主循环
- 用 Pydantic 定义笔记模型
- 用 JSON 文件持久化
- 用 `httpx` 异步调用 LLM API
- 完善的异常处理（文件不存在、API 失败、输入不合法）
- 用类型注解标注所有函数

### 产出物
- `notes_cli.py` — 可直接运行的完整程序
- `notes.json` — 运行后自动生成的数据文件
- `README.md` — 说明用法

### 验收标准
- [ ] `python notes_cli.py` 能看到菜单并能交互操作
- [ ] 添加的笔记关闭程序后再打开仍然存在（JSON 持久化）
- [ ] AI 总结功能能成功调用 LLM 并返回结果
- [ ] 代码有完整的类型注解和异常处理

---

## 推荐学习资源

### 在线教程（免费）
| 资源 | 适合什么 |
|------|---------|
| [Python 官方教程（中文）](https://docs.python.org/zh-cn/3/tutorial/) | 系统学习，有中文 |
| [roadmap.sh/python](https://roadmap.sh/python) | 看路线图，知道该学什么 |
| [realpython.com](https://realpython.com/) | 高质量实战教程（英文） |
| [freeCodeCamp Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) | 交互式练习，免费 |

### GitHub 仓库
| 仓库 | 说明 |
|------|------|
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 微软出的 AI 入门课，含 Python + LLM 基础 |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | PydanticAI 官方仓库，有丰富的 example 代码 |
| [kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) | Python 开发者路线图，350k+ star |

### 关键库文档
| 库 | 文档 | 在 Agent 开发中的作用 |
|----|------|----------------------|
| Pydantic | [docs.pydantic.dev](https://docs.pydantic.dev/) | 定义所有数据模型，输入输出校验 |
| httpx | [www.python-httpx.org](https://www.python-httpx.org/) | 异步 HTTP 客户端，调 LLM API |
| asyncio | [docs.python.org](https://docs.python.org/3/library/asyncio.html) | Python 内置异步库 |

---

## 学习节奏建议

| 周次 | 完成任务 | 预计时间（每天 2h） |
|------|---------|-------------------|
| 第 1 周 | 任务 1-3：环境 + 基础类型 + 容器 | 5 天 |
| 第 2 周 | 任务 4-6：函数 + 文件IO + 异常处理 | 5 天 |
| 第 3 周 | 任务 7-8：异步编程 + Pydantic（重点周！）| 5 天 |
| 第 4 周 | 任务 9-10：API 调用 + 综合实战 | 5 天 |

> **每周末必须有一次完整复盘**，确认当周所有代码能跑通。
> **不要跳过任何任务**——每个任务都是后面写 Agent 时的依赖。

---

## 阶段 0 完成后的你应该能

- [ ] 独立搭建 Python 项目（venv + pip）
- [ ] 写带类型注解的 async 函数
- [ ] 用 Pydantic 定义和校验数据模型
- [ ] 用 httpx 异步调用 HTTP API（包括 LLM API）
- [ ] 处理 JSON 数据的读写和转换
- [ ] 写出有异常处理和重试逻辑的健壮代码
- [ ] 完成"个人知识助手 CLI"综合项目

**全部打勾后，进入阶段 1：LLM 原理与 API 调用。**
