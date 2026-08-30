from abc import ABC, abstractmethod

class BaseRetrievalStrategy(ABC):
    @abstractmethod
    def retrieval_context(self, query: str, limit: int = 3) -> str:
        pass