import logging
import multiprocessing

from queues import Queue
from schemas import Message

logger = logging.getLogger(__name__)


class MultiprocessQueue(Queue):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._queue = multiprocessing.Queue(*args, **kwargs)

    def get(self) -> Message | None:
        if self._queue.empty():
            return None
        return self._queue.get()

    def put(self, message: Message):
        self._queue.put(message)
