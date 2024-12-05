import logging

from config import QUEUE_FILTER_TO_SCREAMING, QUEUE_SCREAMING_TO_SENDING, LOG_LEVEL, LOG_FORMAT
from processors.screaming import ScreamingProcessor
from queues.rabbitmq import RabbitMQQueue

logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


def main():
    input_queue = RabbitMQQueue(QUEUE_FILTER_TO_SCREAMING)
    output_queue = RabbitMQQueue(QUEUE_SCREAMING_TO_SENDING)

    processor = ScreamingProcessor(input_queue=input_queue, output_queues=[output_queue])
    processor.start()
    processor.join()


if __name__ == "__main__":
    main()
