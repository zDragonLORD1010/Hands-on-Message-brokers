import logging
from abc import ABC, abstractmethod
from multiprocessing import Process

from queues import Queue
from schemas import Message

logger = logging.getLogger(__name__)


class Processor(ABC):
    def __init__(self, input_queue: Queue | None = None, output_queues: list[Queue] | None = None):
        self.is_running: bool = False

        self.input_queue: Queue | None = input_queue
        self.output_queues: list[Queue] = [] if output_queues is None else output_queues
        self.current_process: Process | None = None

    def start(self):
        self.is_running = True

        self.current_process = Process(target=self.run)
        self.current_process.start()

        return self.current_process

    def join(self):
        if self.current_process is not None:
            self.current_process.join()

    def stop(self):
        self.is_running = False
        if self.current_process is not None:
            self.current_process.terminate()

    def run(self):
        while self.is_running:
            self.process()

    def process(self):
        message = self.get_input_message()

        if message is None:
            return

        processed_message = self.process_message(message)

        if processed_message is None:
            return

        self.put_output_message(processed_message)

    def get_input_message(self) -> Message | None:
        message = self.input_queue.get() if self.input_queue is not None else None

        if message is not None:
            logger.info(f"Processor {self.__class__.__name__} got message: {message}")

        return message

    def put_output_message(self, message: Message):
        logger.info(f"Processor {self.__class__.__name__} put message: {message}")

        for output_queue in self.output_queues:
            output_queue.put(message)

    @abstractmethod
    def process_message(self, message: Message) -> Message | None:
        pass
