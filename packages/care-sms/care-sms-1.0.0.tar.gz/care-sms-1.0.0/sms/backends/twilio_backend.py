"""
Backend for sending SMS via Twilio.
"""
from typing import List
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from sms.backends.base import SmsBackendBase
from sms.message import TextMessage

try:
    from twilio.rest import Client
    HAS_TWILIO = True
except ImportError:
    HAS_TWILIO = False

class TwilioBackend(SmsBackendBase):
    """
    Handles SMS sending through the Twilio service.
    """
    def __init__(self, fail_silently: bool = False, **kwargs) -> None:
        super().__init__(fail_silently=fail_silently, **kwargs)

        if not HAS_TWILIO and not self.fail_silently:
            raise ImproperlyConfigured("Twilio SDK is required but not installed.")

        self.account_sid = getattr(settings, "TWILIO_ACCOUNT_SID", None)
        self.auth_token = getattr(settings, "TWILIO_AUTH_TOKEN", None)

        if not self.account_sid or not self.auth_token:
            raise ImproperlyConfigured(
                "Missing Twilio credentials. Configure 'TWILIO_ACCOUNT_SID' and 'TWILIO_AUTH_TOKEN'."
            )

        self.client = Client(self.account_sid, self.auth_token) if HAS_TWILIO else None

    def send_messages(self, messages: List[TextMessage]) -> int:
        if not self.client:
            return 0

        successful_sends = 0
        for message in messages:
            for recipient in message.recipients:
                try:
                    self.client.messages.create(
                        body=message.content,
                        from_=message.sender,
                        to=recipient
                    )
                    successful_sends += 1
                except Exception as error:
                    if not self.fail_silently:
                        raise error
        return successful_sends