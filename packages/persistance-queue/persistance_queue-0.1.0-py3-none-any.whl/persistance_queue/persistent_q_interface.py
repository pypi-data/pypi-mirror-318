from abc import ABC, abstractmethod
from typing import Any

class PersistentQInterface(ABC):
    @abstractmethod
    def put(self, job: str) -> None:
        """Put a job into the queue."""
        pass

    @abstractmethod
    def get(self) -> str:
        """Get a job from the queue."""
        pass

    @abstractmethod
    def delete(self, job: str) -> None:
        """Delete a job from the queue."""
        pass

    @abstractmethod
    def size(self) -> int:
        """Get the size of the queue."""
        pass