import logging

from config import STOP_WORDS
from processors import Processor
from schemas import Message

logger = logging.getLogger(__name__)


class FilterProcessor(Processor):
    def process_message(self, message: Message) -> Message | None:
        for stop_word in STOP_WORDS:
            if stop_word in message.text:
                return None

        return message
