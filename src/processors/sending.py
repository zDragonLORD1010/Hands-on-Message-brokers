import logging
import smtplib
from email.mime.text import MIMEText

from config import SMTP_EMAIL, SMTP_RECEIVERS, SMTP_SERVER, SMTP_PORT, SMTP_PASSWORD
from processors import Processor
from schemas import Message

logger = logging.getLogger(__name__)


class SendingProcessor(Processor):
    @staticmethod
    def prepare_email_message(message: Message) -> MIMEText:
        email_text = f"From user: {message.user}\nMessage: {message.text}"
        email_subject = f"Message from {message.user}"

        email_message = MIMEText(email_text)
        email_message["Subject"] = email_subject
        email_message["From"] = SMTP_EMAIL
        email_message["To"] = ", ".join(SMTP_RECEIVERS)

        return email_message

    def process_message(self, message: Message) -> None:
        email_message = self.prepare_email_message(message)

        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_EMAIL, SMTP_PASSWORD)
                server.sendmail(SMTP_EMAIL, SMTP_RECEIVERS, email_message.as_string())
        except Exception as e:
            logger.error(f"Failed to send email: {e}")

        return None
