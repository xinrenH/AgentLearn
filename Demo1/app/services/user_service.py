from app.repositories.memory import MemoryRepo


class UserService:
    @staticmethod
    def create_user(name: str) -> dict:
        user = {"id": len(MemoryRepo.users) + 1, "name": name}
        MemoryRepo.users.append(user)
        return user

    @staticmethod
    def list_users() -> list[dict]:
        return MemoryRepo.users
