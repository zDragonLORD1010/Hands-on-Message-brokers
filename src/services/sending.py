import logging

from config import QUEUE_SCREAMING_TO_SENDING, LOG_LEVEL, LOG_FORMAT
from processors.sending import SendingProcessor
from queues.rabbitmq import RabbitMQQueue

logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


def main():
    input_queue = RabbitMQQueue(QUEUE_SCREAMING_TO_SENDING)

    processor = SendingProcessor(input_queue=input_queue)
    processor.start()
    processor.join()


if __name__ == "__main__":
    main()
