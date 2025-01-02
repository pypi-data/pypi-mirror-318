from typing import Type, Optional, List, TYPE_CHECKING
from django.conf import settings
from sms.signals import sms_sent

if TYPE_CHECKING:
    from sms.backends.base import SmsBackendBase

class TextMessage:
    """
    Represents a text message for transmission to one or more recipients.
    """

    def __init__(
        self,
        content: str = "",
        sender: Optional[str] = None,
        recipients: Optional[List[str]] = None,
        backend: Optional[Type['SmsBackendBase']] = None,
    ) -> None:
        """
        Initialize a TextMessage instance.

        Args:
            content (str): The message content.
            sender (Optional[str]): The sender's phone number.
            recipients (Optional[List[str]]): List of recipient phone numbers.
            backend (Optional[Type['SmsBackendBase']]): Backend for sending the message.
        """
        self.content = content
        self.sender = sender or getattr(settings, "DEFAULT_SMS_SENDER", "")
        self.recipients = recipients or []
        self.backend = backend

        if isinstance(self.recipients, str):
            raise ValueError("Recipients should be a list of phone numbers.")

    def establish_backend(self, silent_fail: bool = False) -> Type['SmsBackendBase']:
        """
        Obtain or initialize the backend for sending messages.

        Args:
            silent_fail (bool): Whether errors should be suppressed.

        Returns:
            SmsBackendBase: An instance of the configured backend.
        """
        from sms import get_sms_backend

        if not self.backend:
            self.backend = get_sms_backend(silent_fail=silent_fail)
        return self.backend

    def dispatch(self, silent_fail: bool = False) -> int:
        """
        Send the message to all designated recipients.

        Args:
            silent_fail (bool): Whether to suppress any errors.

        Returns:
            int: Count of successfully sent messages.
        """
        if not self.recipients:
            return 0

        connection = self.establish_backend(silent_fail)
        sent_count = connection.send_messages([self])

        sms_sent.send(sender=self.__class__, instance=self)
        return sent_count