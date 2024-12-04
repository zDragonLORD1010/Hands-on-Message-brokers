import logging

from config import LOG_LEVEL, LOG_FORMAT
from processors.api import APIProcessor
from processors.filter import FilterProcessor
from processors.screaming import ScreamingProcessor
from processors.sending import SendingProcessor
from queues.multiprocess import MultiprocessQueue

logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
logger = logging.getLogger(__name__)

queue_api_to_filter = MultiprocessQueue()
queue_filter_to_screaming = MultiprocessQueue()
queue_screaming_to_sending = MultiprocessQueue()

api_processor = APIProcessor(
    output_queues=[queue_api_to_filter]
)
filter_processor = FilterProcessor(
    input_queue=queue_api_to_filter,
    output_queues=[queue_filter_to_screaming]
)
screaming_processor = ScreamingProcessor(
    input_queue=queue_filter_to_screaming,
    output_queues=[queue_screaming_to_sending]
)
sending_processor = SendingProcessor(
    input_queue=queue_screaming_to_sending
)

processors = [
    api_processor,
    filter_processor,
    screaming_processor,
    sending_processor
]


def main():
    for processor in processors:
        processor.start()

    for processor in processors:
        processor.join()


if __name__ == "__main__":
    main()
