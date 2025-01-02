"""
Dummy SMS backend that does nothing.
"""
from typing import List
from sms.backends.base import SmsBackendBase
from sms.message import TextMessage

class DummyBackend(SmsBackendBase):
    """
    A no-op backend for testing purposes.
    """
    def send_messages(self, messages: List[TextMessage]) -> int:
        return len(messages)