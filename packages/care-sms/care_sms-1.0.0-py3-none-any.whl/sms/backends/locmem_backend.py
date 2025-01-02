"""
In-memory SMS backend for testing.
"""
from typing import List
import sms
from sms.backends.base import SmsBackendBase
from sms.message import TextMessage


class LocMemBackend(SmsBackendBase):
    """
    Stores messages in a dummy outbox attached to the `sms` module.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if not hasattr(sms, 'outbox'):
            sms.outbox = []  # Initialize outbox on the `sms` module

    def send_messages(self, messages: List[TextMessage]) -> int:
        """Redirect messages to the dummy outbox."""
        sms.outbox.extend(messages)
        return len(messages)
