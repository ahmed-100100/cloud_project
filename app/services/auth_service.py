from abc import ABC, abstractmethod

class AuthService(ABC):
    @abstractmethod
    def hash_password(self, password: str) -> str:
        pass

    @abstractmethod
    def verify_password(self, plain: str, hashed: str) -> bool:
        pass

    @abstractmethod
    def create_token(self, user_id: int) -> str:
        pass
