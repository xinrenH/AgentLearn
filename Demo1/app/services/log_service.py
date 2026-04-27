from app.repositories.memory import MemoryRepo


class LogService:
    @staticmethod
    def add_log(content: str) -> dict:
        log = {"id": len(MemoryRepo.logs) + 1, "content": content}
        MemoryRepo.logs.append(log)
        return log

    @staticmethod
    def list_logs() -> list[dict]:
        return MemoryRepo.logs
