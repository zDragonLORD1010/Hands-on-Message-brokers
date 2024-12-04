import logging

from config import QUEUE_API_TO_FILTER, QUEUE_FILTER_TO_SCREAMING, LOG_LEVEL, LOG_FORMAT
from processors.filter import FilterProcessor
from queues.rabbitmq import RabbitMQQueue

logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


def main():
    input_queue = RabbitMQQueue(QUEUE_API_TO_FILTER)
    output_queue = RabbitMQQueue(QUEUE_FILTER_TO_SCREAMING)

    processor = FilterProcessor(input_queue=input_queue, output_queues=[output_queue])
    processor.start()
    processor.join()


if __name__ == "__main__":
    main()
