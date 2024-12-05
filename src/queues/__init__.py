from abc import ABC, abstractmethod

from schemas import Message


class Queue(ABC):
    @abstractmethod
    def get(self) -> Message | None:
        pass

    @abstractmethod
    def put(self, message: Message):
        pass
