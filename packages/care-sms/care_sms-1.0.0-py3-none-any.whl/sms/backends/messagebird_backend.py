"""
Backend for sending SMS via MessageBird.
"""
from typing import List
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from sms.backends.base import SmsBackendBase
from sms.message import TextMessage

try:
    import messagebird
    HAS_MESSAGEBIRD = True
except ImportError:
    HAS_MESSAGEBIRD = False

class MessageBirdBackend(SmsBackendBase):
    """
    Handles SMS sending through the MessageBird API.
    """
    def __init__(self, fail_silently: bool = False, **kwargs) -> None:
        super().__init__(fail_silently=fail_silently, **kwargs)

        if not HAS_MESSAGEBIRD and not self.fail_silently:
            raise ImproperlyConfigured("MessageBird SDK is required but not installed.")

        self.access_key = getattr(settings, "MESSAGEBIRD_ACCESS_KEY", None)

        if not self.access_key:
            raise ImproperlyConfigured(
                "Missing MessageBird API key. Configure 'MESSAGEBIRD_ACCESS_KEY'."
            )

        self.client = messagebird.Client(self.access_key) if HAS_MESSAGEBIRD else None

    def send_messages(self, messages: List[TextMessage]) -> int:
        if not self.client:
            return 0

        successful_sends = 0
        for message in messages:
            try:
                self.client.message_create(
                    sender=message.sender,
                    recipients=message.recipients,
                    body=message.content
                )
                successful_sends += len(message.recipients)
            except Exception as error:
                if not self.fail_silently:
                    raise error
        return successful_sends