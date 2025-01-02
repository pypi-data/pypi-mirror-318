"""
Utilities for managing text message backends and sending messages.
"""
from typing import List, Optional, Type, Union
from django.conf import settings
from django.utils.module_loading import import_string
from sms.backends.base import SmsBackendBase
from sms.message import TextMessage

__all__ = [
    "TextMessage", "initialize_backend", "send_text_message"
]

def initialize_backend(
    backend_name: Optional[str] = None,
    suppress_errors: bool = False,
    **kwargs
) -> Type[SmsBackendBase]:
    """
    Load and configure an SMS backend.

    Args:
        backend_name (Optional[str]): The dotted path to the backend class.
        suppress_errors (bool): Whether to handle exceptions quietly.

    Returns:
        SmsBackendBase: An initialized backend instance.
    """
    backend_class = import_string(backend_name or settings.SMS_BACKEND)
    return backend_class(fail_silently=suppress_errors, **kwargs)

def send_text_message(
    content: str = "",
    sender: Optional[str] = None,
    recipients: Union[Optional[str], Optional[List[str]]] = None,
    suppress_errors: bool = False,
    backend_instance: Optional[Type[SmsBackendBase]] = None
) -> int:
    """
    Simplified function for sending a single message to recipients.

    Args:
        content (str): The message content.
        sender (Optional[str]): The sender's phone number.
        recipients (Union[Optional[str], Optional[List[str]]]):
            A single recipient or a list of recipients.
        suppress_errors (bool): Whether to suppress any exceptions.
        backend_instance (Optional[Type[SmsBackendBase]]): A preconfigured backend instance.

    Returns:
        int: The number of messages successfully sent.
    """
    if isinstance(recipients, str):
        recipients = [recipients]
    message = TextMessage(content=content, sender=sender, recipients=recipients, backend=backend_instance)
    return message.dispatch(silent_fail=suppress_errors)


def get_sms_backend(
    backend_name: Optional[str] = None,
    suppress_errors: bool = False,
    **kwargs
) -> SmsBackendBase:
    """
    Load and return an SMS backend instance.

    Args:
        backend_name (Optional[str]): The dotted path to the backend class.
        suppress_errors (bool): Whether to handle exceptions quietly.
        **kwargs: Additional arguments passed to the backend.

    Returns:
        SmsBackendBase: An initialized backend instance.
    """
    return initialize_backend(
        backend_name=backend_name or settings.SMS_BACKEND,
        suppress_errors=suppress_errors,
        **kwargs
    )
