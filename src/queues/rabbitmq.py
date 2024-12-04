import logging

import pika

from config import RABBITMQ_HOST, RABBITMQ_PORT
from queues import Queue
from schemas import Message

logger = logging.getLogger(__name__)


class RabbitMQQueue(Queue):
    def __init__(self, queue_name):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT)
        )
        self.channel = self.connection.channel()
        self.queue_name = queue_name
        self.channel.queue_declare(queue=queue_name, durable=True)

    def get(self) -> Message | None:
        method_frame, header_frame, body = self.channel.basic_get(queue=self.queue_name, auto_ack=True)
        if method_frame:
            return Message.model_validate_json(body)
        return None

    def put(self, message: Message):
        self.channel.basic_publish(
            exchange="",
            routing_key=self.queue_name,
            body=message.model_dump_json(),
            properties=pika.BasicProperties(delivery_mode=2)
        )
