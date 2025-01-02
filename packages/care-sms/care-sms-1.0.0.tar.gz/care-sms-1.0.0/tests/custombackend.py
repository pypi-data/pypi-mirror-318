"""A custom backend for testing."""

from typing import List

from sms.backends.base import SmsBackendBase
from sms.message import TextMessage


class CustomBackend(SmsBackendBase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.test_outbox: List[TextMessage] = []

    def send_messages(self, messages: List[TextMessage]) -> int:
        # Messages are stored in an instance variable for testing
        self.test_outbox.extend(messages)
        return len(messages)
