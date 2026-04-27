from app.repositories.memory import MemoryRepo


class TaskService:
    @staticmethod
    def create_task(title: str) -> dict:
        task = {"id": len(MemoryRepo.tasks) + 1, "title": title, "status": "todo"}
        MemoryRepo.tasks.append(task)
        return task

    @staticmethod
    def list_tasks() -> list[dict]:
        return MemoryRepo.tasks

    @staticmethod
    def update_status(task_id: int, status: str) -> dict | None:
        for t in MemoryRepo.tasks:
            if t["id"] == task_id:
                t["status"] = status
                return t
        return None
