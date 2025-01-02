# Care SMS - Backend Configuration for Django Apps

Care SMS supports multiple SMS backends for sending messages. Each backend is designed for specific use cases like testing, development, or production. Here's how you can configure and use each backend in a Django project:

---

## **1. Setting Up the Backend**
To configure an SMS backend in a Django app, add the `SMS_BACKEND` setting in your `settings.py` file.

Example:
```python
# settings.py
SMS_BACKEND = 'sms.backends.<backend_module>.<BackendClass>'
```

---

## **2. Dummy Backend**
The Dummy Backend does nothing with the messages and is useful for testing.

**Configuration:**
```python
# settings.py
SMS_BACKEND = 'sms.backends.dummy_backend.DummyBackend'
```

**Usage:**
```python
from sms import send_text_message

send_text_message('Test Message', 'Sender', ['Recipient'])
```

---

## **3. LocMem Backend**
The LocMem Backend stores messages in an in-memory outbox, ideal for testing without external dependencies.

**Configuration:**
```python
# settings.py
SMS_BACKEND = 'sms.backends.locmem_backend.LocMemBackend'
```

**Accessing the Outbox:**
```python
from sms.backends.locmem_backend import outbox

print(outbox)  # List of sent messages
```

**Usage:**
```python
from sms import send_text_message

send_text_message('Test Message', 'Sender', ['Recipient'])
```

---

## **4. Console Backend**
The Console Backend writes messages to the console or a custom stream. This backend is useful during development.

**Configuration:**
```python
# settings.py
SMS_BACKEND = 'sms.backends.console_backend.ConsoleBackend'
```

**Usage:**
```python
from sms import send_text_message

send_text_message('Test Message', 'Sender', ['Recipient'])
```

---

## **5. File-Based Backend**
The File-Based Backend saves messages to files in a specified directory, useful for debugging or lightweight persistence.

**Configuration:**
```python
# settings.py
SMS_BACKEND = 'sms.backends.file_backend.FileBackend'
SMS_FILE_PATH = '/path/to/log/directory'
```

**Usage:**
```python
from sms import send_text_message

send_text_message('Test Message', 'Sender', ['Recipient'])
```

---

## **6. MessageBird Backend**
The MessageBird Backend sends SMS via the MessageBird API. Requires an API key.

**Configuration:**
```python
# settings.py
SMS_BACKEND = 'sms.backends.messagebird_backend.MessageBirdBackend'
MESSAGEBIRD_ACCESS_KEY = 'your_messagebird_access_key'
```

**Usage:**
```python
from sms import send_text_message

send_text_message('Test Message', 'Sender', ['Recipient'])
```

---

## **7. Twilio Backend**
The Twilio Backend sends SMS via the Twilio API. Requires account credentials.

**Configuration:**
```python
# settings.py
SMS_BACKEND = 'sms.backends.twilio_backend.TwilioBackend'
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
```

**Usage:**
```python
from sms import send_text_message

send_text_message('Test Message', 'Sender', ['Recipient'])
```

---

## **8. AWS SNS Backend**
The AWS SNS Backend sends SMS via AWS SNS. Requires AWS credentials and configuration.

**Configuration:**
```python
# settings.py
SMS_BACKEND = 'sms.backends.aws_backend.SnsBackend'
AWS_SNS_REGION = 'your_region'
AWS_SNS_ACCESS_KEY_ID = 'your_access_key_id'
AWS_SNS_SECRET_ACCESS_KEY = 'your_secret_access_key'
AWS_SNS_SENDER_ID = 'your_sender_id'
AWS_SNS_SMS_TYPE = 'Transactional'  # or 'Promotional'
```

**Usage:**
```python
from sms import send_text_message

send_text_message('Test Message', 'Sender', ['Recipient'])
```

---

## **Sending SMS**
Once configured, use the `send_text_message` function to send SMS:
```python
from sms import send_text_message

send_text_message('Hello, World!', 'SenderID', ['+1234567890'])
```

This function uses the configured backend automatically.

---
