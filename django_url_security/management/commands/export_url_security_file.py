from django.core.management.base import BaseCommand

from django_url_security.core import DEFAULT_URL_SECURITY_SPEC_FILE_PATH
from django_url_security.generate_permission_spec_file import (
    print_permission_spec_file,
)


class Command(BaseCommand):
    help = f'Writes the current permission specifications to {DEFAULT_URL_SECURITY_SPEC_FILE_PATH}'

    def handle(self, *args, **options):
        print_permission_spec_file()
