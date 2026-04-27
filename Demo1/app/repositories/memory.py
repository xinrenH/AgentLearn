from typing import Any


class MemoryRepo:
    users: list[dict[str, Any]] = []
    tasks: list[dict[str, Any]] = []
    logs: list[dict[str, Any]] = []
