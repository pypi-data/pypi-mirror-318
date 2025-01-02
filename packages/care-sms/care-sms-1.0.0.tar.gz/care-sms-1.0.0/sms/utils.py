import re
from sms.message import TextMessage

HEADER_PATTERN = re.compile(r"^(?:from|to): .*")
FROM_HEADER_PATTERN = re.compile(r"^from: (.*)$", re.MULTILINE)
TO_HEADER_PATTERN = re.compile(r"^to: (.*)$", re.MULTILINE)

def parse_message_from_file(file_pointer) -> TextMessage:
    """
    Create a TextMessage object by reading a binary file.

    Args:
        file_pointer: File pointer to the binary message file.

    Returns:
        TextMessage: A parsed TextMessage instance.
    """
    return parse_message_from_bytes(file_pointer.read())

def parse_message_from_bytes(data: bytes) -> TextMessage:
    """
    Parse a bytestring to create a TextMessage object.

    Args:
        data (bytes): Binary data containing message details.

    Returns:
        TextMessage: A populated TextMessage instance.

    Raises:
        ValueError: If mandatory headers are missing.
    """
    decoded_text = data.decode("ASCII", errors="surrogateescape")

    body = ""
    for line in decoded_text.splitlines():
        if not HEADER_PATTERN.match(line):
            body += f"\n{line}" if body else line

    from_match = FROM_HEADER_PATTERN.search(decoded_text)
    if not from_match:
        raise ValueError("'From' header is missing.")
    sender = from_match.group(1)

    to_match = TO_HEADER_PATTERN.search(decoded_text)
    if not to_match:
        raise ValueError("'To' header is missing.")
    recipients = [to_match.group(1)]

    return TextMessage(content=body, sender=sender, recipients=recipients)