import logging

import pika

from config import RABBITMQ_HOST, RABBITMQ_PORT
from queues import Queue
from schemas import Message

logger = logging.getLogger(__name__)


class RabbitMQQueue(Queue):
    def __init__(self, queue_name):
        self.queue_name = queue_name

        self.connection = None
        self.channel = None
        self.channel = None

        self.connect()

    def connect(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT)
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name, durable=True)

    def get(self) -> Message | None:
        if self.connection.is_closed or self.channel.is_closed:
            self.connect()

        method_frame, header_frame, body = self.channel.basic_get(queue=self.queue_name, auto_ack=True)
        if method_frame:
            return Message.model_validate_json(body)
        return None

    def put(self, message: Message):
        if self.connection.is_closed or self.channel.is_closed:
            self.connect()

        self.channel.basic_publish(
            exchange="",
            routing_key=self.queue_name,
            body=message.model_dump_json(),
            properties=pika.BasicProperties(delivery_mode=2)
        )
