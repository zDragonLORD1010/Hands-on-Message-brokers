import logging

from processors import Processor
from schemas import Message

logger = logging.getLogger(__name__)


class ScreamingProcessor(Processor):
    def process_message(self, message: Message) -> Message:
        return Message(user=message.user, text=message.text.upper())
