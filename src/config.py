from os import getenv

QUEUE_API_TO_FILTER = "api_to_filter"
QUEUE_FILTER_TO_SCREAMING = "filter_to_screaming"
QUEUE_SCREAMING_TO_SENDING = "screaming_to_sending"

LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(filename)s - %(message)s"

API_HOST = "0.0.0.0"
API_PORT = 8000

RABBITMQ_HOST = "rabbitmq"
RABBITMQ_PORT = 5672

STOP_WORDS = ["bird-watching", "ailurophobia", "mango"]

SMTP_SERVER = getenv("SMTP_SERVER").strip()
SMTP_PORT = int(getenv("SMTP_PORT").strip())
SMTP_EMAIL = getenv("SMTP_EMAIL").strip()
SMTP_PASSWORD = getenv("SMTP_PASSWORD").strip()
SMTP_RECEIVERS = [
    smtp_receiver.strip() for smtp_receiver in getenv("SMTP_RECEIVERS").split(",")
]
