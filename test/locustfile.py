from random import randint

from locust import HttpUser, constant_throughput, task, between


class MessageTestUser(HttpUser):
    wait_time = between(0.5, 2)

    @task
    def send_message(self):
        message = {
            "user": f"user{randint(1, 1000)}",
            "text": f"Message about {randint(1, 1000)} things",
        }
        self.client.post("/messages", json=message)
