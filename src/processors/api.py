import logging

import uvicorn
from fastapi import FastAPI, HTTPException
from typing_extensions import override

from config import API_HOST, API_PORT
from processors import Processor
from schemas import Message

logger = logging.getLogger(__name__)


class APIProcessor(Processor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = FastAPI()

        self.app.add_api_route("/messages", self.create_new_message, methods=["POST"])

    @override
    def run(self):
        uvicorn.run(self.app, host=API_HOST, port=API_PORT)

    async def create_new_message(self, message: Message):
        try:
            self.put_output_message(message)

            return {"message": "Message sent"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to send message: {str(e)}")

    def process_message(self, message: Message) -> Message | None:
        return message
