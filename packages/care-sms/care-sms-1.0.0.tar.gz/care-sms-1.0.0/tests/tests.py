import os
import sys
import shutil
import tempfile
from typing import List, Type, Optional
from io import StringIO
from unittest.mock import MagicMock
from django.dispatch import receiver
from django.test import SimpleTestCase, override_settings
import sms
from sms import send_text_message
from sms.backends import dummy_backend, locmem_backend, file_backend
from sms.backends.base import SmsBackendBase
from sms.message import TextMessage
from sms.signals import sms_sent
from sms.utils import parse_message_from_bytes, parse_message_from_file

class BaseSmsBackendTests:
    sms_backend: Optional[str] = None

    def setUp(self) -> None:
        self.settings_override = override_settings(SMS_BACKEND=self.sms_backend)
        self.settings_override.enable()

    def tearDown(self) -> None:
        self.settings_override.disable()

class SmsTests(SimpleTestCase):

    def test_dummy_backend(self) -> None:
        connection = dummy_backend.DummyBackend()
        message = TextMessage()
        self.assertEqual(connection.send_messages([message, message, message]), 3)

    def test_backend_arg(self) -> None:
        self.assertIsInstance(
            sms.initialize_backend('sms.backends.dummy_backend.DummyBackend'),
            dummy_backend.DummyBackend
        )
        with tempfile.TemporaryDirectory() as tmp_dir:
            self.assertIsInstance(
                sms.initialize_backend('sms.backends.file_backend.FileBackend', file_path=tmp_dir),
                file_backend.FileBackend
            )
        msg = 'expected str, bytes or os.PathLike object, not object'
        with self.assertRaisesMessage(TypeError, msg):
            sms.initialize_backend('sms.backends.file_backend.FileBackend', file_path=object())
        self.assertIsInstance(sms.initialize_backend(), locmem_backend.LocMemBackend)

    def test_custom_backend(self) -> None:
        connection = sms.initialize_backend('tests.custombackend.CustomBackend')
        self.assertTrue(hasattr(connection, 'test_outbox'))
        message = TextMessage('Content', '0600000000', ['0600000000'])
        connection.send_messages([message])
        self.assertEqual(len(connection.test_outbox), 1)

    @override_settings(SMS_BACKEND='sms.backends.locmem_backend.LocMemBackend')
    def test_send_sms(self) -> None:
        send_text_message('Content', '0600000000', '0600000000')
        self.assertEqual(len(sms.outbox), 1)
        self.assertIsInstance(sms.outbox[0].recipients, list)

class LocmemBackendTests(BaseSmsBackendTests, SimpleTestCase):
    sms_backend: str = 'sms.backends.locmem_backend.LocMemBackend'

    def flush_mailbox(self) -> None:
        sms.outbox = []

    def tearDown(self) -> None:
        super().tearDown()
        self.flush_mailbox()

    def test_locmem_shared_messages(self) -> None:
        connections: List[Type[SmsBackendBase]] = [
            locmem_backend.LocMemBackend(),
            locmem_backend.LocMemBackend()
        ]
        message = TextMessage('Content', '0600000000', ['0600000000'])
        for connection in connections:
            connection.send_messages([message])
        self.assertEqual(len(sms.outbox), 2)

class ConsoleBackendTests(BaseSmsBackendTests, SimpleTestCase):
    sms_backend: str = 'sms.backends.console_backend.ConsoleBackend'

    def test_console_stream_kwarg(self) -> None:
        stream = StringIO()
        connection = sms.initialize_backend('sms.backends.console_backend.ConsoleBackend', stream=stream)
        message = TextMessage('Content', '0600000000', ['0600000000'])
        connection.send_messages([message])
        messages = stream.getvalue().split('\n' + ('-' * 79) + '\n')
        self.assertIn('From: ', messages[0])

class FileBasedBackendTests(BaseSmsBackendTests, SimpleTestCase):
    sms_backend = 'sms.backends.file_backend.FileBackend'

    def setUp(self) -> None:
        super().setUp()
        self.tmp_dir = self.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp_dir)
        self._settings_override = override_settings(SMS_FILE_PATH=self.tmp_dir)
        self._settings_override.enable()

    def tearDown(self) -> None:
        self._settings_override.disable()
        super().tearDown()

    def mkdtemp(self) -> str:
        return tempfile.mkdtemp()

    def flush_mailbox(self) -> None:
        for filename in os.listdir(self.tmp_dir):
            os.unlink(os.path.join(self.tmp_dir, filename))

    def get_mailbox_content(self) -> List[TextMessage]:
        messages: List[TextMessage] = []
        for filename in os.listdir(self.tmp_dir):
            with open(os.path.join(self.tmp_dir, filename), 'rb') as fp:
                session = fp.read().split(b'\n' + (b'-' * 79) + b'\n')
            messages.extend(parse_message_from_bytes(m) for m in session if m)
        return messages

    def test_file_sessions(self) -> None:
        message = TextMessage('Here is the message', '+12065550100', ['+441134960000'])
        connection = sms.initialize_backend('sms.backends.file_backend.FileBackend', file_path=self.tmp_dir)
        connection.send_messages([message])

        self.assertEqual(len(os.listdir(self.tmp_dir)), 1)
        tmp_file = os.path.join(self.tmp_dir, os.listdir(self.tmp_dir)[0])
        with open(tmp_file, 'r') as fp:
            file_content = fp.read()
        self.assertIn("From: +12065550100", file_content)
        self.assertIn("To: +441134960000", file_content)
        self.assertIn("Content: Here is the message", file_content)

class MessageBirdBackendTests(BaseSmsBackendTests, SimpleTestCase):
    sms_backend = 'sms.backends.messagebird_backend.MessageBirdBackend'

    def setUp(self) -> None:
        super().setUp()
        self._settings_override = override_settings(MESSAGEBIRD_ACCESS_KEY='fake_access_key')
        self._settings_override.enable()

    def tearDown(self) -> None:
        self._settings_override.disable()
        super().tearDown()

    def test_send_messages(self) -> None:
        message = TextMessage('Here is the message', '+12065550100', ['+441134960000'])
        connection = sms.initialize_backend('sms.backends.messagebird_backend.MessageBirdBackend')
        connection.client.message_create = MagicMock()
        connection.send_messages([message])
        connection.client.message_create.assert_called_with(
            sender='+12065550100',
            recipients=['+441134960000'],
            body='Here is the message'
        )

class TwilioBackendTests(BaseSmsBackendTests, SimpleTestCase):
    sms_backend = 'sms.backends.twilio_backend.TwilioBackend'

    def setUp(self) -> None:
        super().setUp()
        self._settings_override = override_settings(
            TWILIO_ACCOUNT_SID='fake_account_sid',
            TWILIO_AUTH_TOKEN='fake_auth_token',
        )
        self._settings_override.enable()

    def tearDown(self) -> None:
        self._settings_override.disable()
        super().tearDown()

    def test_send_messages(self) -> None:
        message = TextMessage('Here is the message', '+12065550100', ['+441134960000'])
        connection = sms.initialize_backend()
        connection.client.messages.create = MagicMock()
        connection.send_messages([message])
        connection.client.messages.create.assert_called_with(
            to='+441134960000',
            from_='+12065550100',
            body='Here is the message'
        )

class AwsBackendTests(BaseSmsBackendTests, SimpleTestCase):
    sms_backend = 'sms.backends.aws_backend.SnsBackend'

    def setUp(self) -> None:
        super().setUp()
        self._settings_override = override_settings(
            AWS_SNS_REGION='us-moon-3',
            AWS_SNS_ACCESS_KEY_ID='AKIAFAKEACCESSKEYID',
            AWS_SNS_SECRET_ACCESS_KEY='fake_secret_access_key',
            AWS_SNS_SENDER_ID='care-sms',
            AWS_SNS_SMS_TYPE='Promotional',
        )
        self._settings_override.enable()

    def tearDown(self) -> None:
        self._settings_override.disable()
        super().tearDown()

    def test_send_messages(self) -> None:
        message = TextMessage(content='Here is the message', sender='+12065550100', recipients=['+441134960000'])
        connection = sms.initialize_backend('sms.backends.aws_backend.SnsBackend')
        connection.sns_client.publish = MagicMock()
        connection.send_messages([message])
        connection.sns_client.publish.assert_called_with(
            PhoneNumber='+441134960000',
            Message='Here is the message',
            MessageAttributes={
                "AWS.SNS.SMS.SenderID": {
                    "DataType": "String",
                    "StringValue": "care-sms",
                },
                "AWS.SNS.SMS.SMSType": {
                    "DataType": "String",
                    "StringValue": "Promotional",
                },
            },
        )

class SignalTests(SimpleTestCase):

    def flush_mailbox(self) -> None:
        sms.outbox = []

    def tearDown(self) -> None:
        super().tearDown()
        self.flush_mailbox()

    def test_receiver_post_send_signal(self) -> None:
        @receiver(sms_sent)
        def f(instance, **kwargs):
            self.body = instance.content
            self.state = True
        self.state = False
        self.body = None

        body = 'Here is the message'
        message = TextMessage(body, '+12065550100', ['+441134960000'])
        message.dispatch()

        self.assertTrue(self.state)
        self.assertEqual(body, self.body)
