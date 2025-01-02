import sys
import django

from django.test.runner import DiscoverRunner
from django.conf import settings


settings.configure(
    DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3'}},
    SECRET_KEY="it's a secret to everyone",
    SMS_BACKEND='sms.backends.locmem_backend.LocMemBackend',
)


def main() -> None:
    django.setup()
    runner = DiscoverRunner(failfast=True, verbosity=1)
    failures = runner.run_tests([], interactive=True)
    sys.exit(failures)


if __name__ == '__main__':
    main()
