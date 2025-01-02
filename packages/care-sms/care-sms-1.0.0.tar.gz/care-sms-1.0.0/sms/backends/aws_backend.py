"""
Backend for sending SMS via AWS SNS.
"""

from typing import List, Optional
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from sms.backends.base import SmsBackendBase
from sms.message import TextMessage

try:
    import boto3
    from botocore.exceptions import ClientError

    HAS_BOTO3 = True
except ImportError:
    HAS_BOTO3 = False


class SnsBackend(SmsBackendBase):
    """
    Handles SMS sending through AWS SNS.
    """

    def __init__(self, fail_silently: bool = False, **kwargs) -> None:
        super().__init__(fail_silently=fail_silently, **kwargs)

        if not HAS_BOTO3 and not self.fail_silently:
            raise ImproperlyConfigured("Boto3 library is required but not installed.")

        self.region_name = getattr(settings, "AWS_SNS_REGION", None)
        self.access_key_id = getattr(settings, "AWS_SNS_ACCESS_KEY_ID", None)
        self.secret_access_key = getattr(settings, "AWS_SNS_SECRET_ACCESS_KEY", None)

        if not self.region_name or not self.access_key_id or not self.secret_access_key:
            raise ImproperlyConfigured(
                "AWS SNS credentials are not fully configured. Check 'AWS_SNS_REGION','AWS_SNS_ACCESS_KEY_ID', and 'AWS_SNS_SECRET_ACCESS_KEY' in settings."
            )

        self.sns_client = None
        if HAS_BOTO3:
            self.sns_client = boto3.client(
                "sns",
                region_name=self.region_name,
                aws_access_key_id=self.access_key_id,
                aws_secret_access_key=self.secret_access_key,
            )

    def send_messages(self, messages: List[TextMessage]) -> int:
        if not self.sns_client:
            return 0

        successful_sends = 0
        for message in messages:
            for recipient in message.recipients:
                try:
                    self.sns_client.publish(
                        PhoneNumber=recipient,
                        Message=message.content,
                        MessageAttributes={
                            "AWS.SNS.SMS.SenderID": {
                                "DataType": "String",
                                "StringValue": getattr(
                                    settings, "AWS_SNS_SENDER_ID", "care-sms"
                                ),
                            },
                            "AWS.SNS.SMS.SMSType": {
                                "DataType": "String",
                                "StringValue": getattr(
                                    settings, "AWS_SNS_SMS_TYPE", "Promotional"
                                ),
                            },
                        },
                    )
                    successful_sends += 1
                except ClientError as error:
                    if not self.fail_silently:
                        raise error
        return successful_sends
