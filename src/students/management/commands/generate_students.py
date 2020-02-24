import random

from django.core.management.base import BaseCommand
from faker import Faker
from students.models import Student, Group


class Command(BaseCommand):
    help = 'Generate random students'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--number',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        Group.objects.all().delete()
        Student.objects.all().delete()
        fake = Faker()

        groups = [Group.objects.create(
            group_name=f'group_{i}',
            # curator=random.choice(teachers),
            start_date=fake.date(pattern="%Y-%m-%d", end_datetime=None)
        )
            for i in range(10)]

        number = int(options.get('number') or 100)
        # for student in Student.objects.all():
        for _ in range(number):
            student = Student.generate_student()
            student.st_group = random.choice(groups)
            student.save()
