import logging

from config import QUEUE_API_TO_FILTER, LOG_LEVEL, LOG_FORMAT
from processors.api import APIProcessor
from queues.rabbitmq import RabbitMQQueue

logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


def main():
    output_queue = RabbitMQQueue(QUEUE_API_TO_FILTER)

    processor = APIProcessor(output_queues=[output_queue])
    processor.start()
    processor.join()


if __name__ == "__main__":
    main()
