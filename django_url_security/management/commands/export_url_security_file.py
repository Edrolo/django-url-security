from django.core.management.base import BaseCommand

from django_url_security.generate_permission_spec_file import print_permission_spec_file


class Command(BaseCommand):
    help = (
        'Writes the current permission specifications to '
        'view_permission_specifications.csv'
    )

    def handle(self, *args, **options):
        print_permission_spec_file()
