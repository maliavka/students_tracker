from django.core.management.base import BaseCommand
from students.models import Group


class Command(BaseCommand):
    help = 'Generate random groups'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--number',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        number = int(options.get('number') or 50)
        for _ in range(number):
            Group.generate_group()
