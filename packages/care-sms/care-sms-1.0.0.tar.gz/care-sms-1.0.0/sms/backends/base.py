"""
Base class for SMS backend implementations.
"""
from typing import Optional, Type, List
from types import TracebackType
from sms.message import TextMessage

class SmsBackendBase:
    """
    Base class for all SMS backends.

    Subclasses should override `send_messages`.
    """
    def __init__(self, fail_silently: bool = False, **kwargs) -> None:
        self.fail_silently = fail_silently

    def open(self) -> bool:
        """
        Open a connection, if applicable.

        Returns:
            bool: Connection status (default is True).
        """
        return True

    def close(self) -> None:
        """
        Close the connection, if applicable.
        """
        pass

    def __enter__(self) -> 'SmsBackendBase':
        self.open()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType]
    ) -> None:
        self.close()

    def send_messages(self, messages: List[TextMessage]) -> int:
        """
        Send one or more text messages.

        Args:
            messages (List[TextMessage]): List of messages to send.

        Raises:
            NotImplementedError: If not implemented in subclass.

        Returns:
            int: Number of messages sent.
        """
        raise NotImplementedError("Subclasses must implement `send_messages`.")