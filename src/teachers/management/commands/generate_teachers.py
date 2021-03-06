from django.core.management.base import BaseCommand
from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generate random teachers'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--number',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        number = int(options.get('number') or 40)
        for _ in range(number):
            Teacher.generate_teacher()
