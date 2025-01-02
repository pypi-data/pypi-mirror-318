"""
SMS backend that writes messages to a file.
"""

import os
import datetime
from typing import Optional, List

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from sms.backends.console_backend import ConsoleBackend
from sms.message import TextMessage


class FileBackend(ConsoleBackend):
    """
    SMS backend that writes messages to a file for storage.
    """

    def __init__(
        self,
        *args,
        file_path: Optional[str] = None,
        **kwargs
    ) -> None:
        """
        Initialize the FileBackend with a file path for saving messages.

        Args:
            file_path (Optional[str]): The directory where messages will be stored.
        """
        super().__init__(*args, **kwargs)

        # Determine the file path from the argument or settings
        file_path = file_path or getattr(settings, "SMS_FILE_PATH", None)
        if not file_path:
            raise ImproperlyConfigured("`file_path` must be specified for FileBackend.")
        
        self.file_path = os.path.abspath(file_path)

        # Ensure the directory exists and is writable
        try:
            os.makedirs(self.file_path, exist_ok=True)
        except FileExistsError:
            raise ImproperlyConfigured(
                f"Path for saving messages exists but is not a directory: {self.file_path}"
            )
        except OSError as exc:
            raise ImproperlyConfigured(
                f"Could not create directory for saving messages: {self.file_path} ({exc})"
            )

        if not os.access(self.file_path, os.W_OK):
            raise ImproperlyConfigured(f"Directory is not writable: {self.file_path}")

    def _get_filename(self) -> str:
        """
        Generate a unique filename for storing messages.

        Returns:
            str: The full path to the file.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        return os.path.join(self.file_path, f"sms-{timestamp}.log")

    def send_messages(self, messages: List[TextMessage]) -> int:
        """
        Write messages to a log file.

        Args:
            messages (List[TextMessage]): The list of messages to send.

        Returns:
            int: The number of messages successfully written.
        """
        with open(self._get_filename(), "a") as file:
            for message in messages:
                for recipient in message.recipients:
                    file.write(
                        f"From: {message.sender}\n"
                        f"To: {recipient}\n"
                        f"Content: {message.content}\n"
                        f"{'-' * 79}\n"
                    )
        return len(messages)
