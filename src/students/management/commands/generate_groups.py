import random

from django.core.management.base import BaseCommand
from faker import Faker
from datetime import datetime
from students.models import Student, Group
from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generate random groups'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--number',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        Group.objects.all().delete()
        Student.objects.all().delete()
        Teacher.objects.all().delete()
        fake = Faker()

        teachers = [Teacher.objects.create(
            teach_name=f'teacher_{j}',
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birth_date=fake.date_of_birth(tzinfo=None, minimum_age=25, maximum_age=65),
            position=fake.job(),
            email=fake.email(),
            telephone=fake.phone_number(),
        ) for j in range(50)]

        students = [Student.objects.create(
            st_name=f'student_{i}',
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birth_date=datetime.now().date(),
            email=fake.email(),
            telephone=fake.phone_number(),

        ) for i in range(100)]

        number = int(options.get('number') or 10)
        for _ in range(number):
            group = Group.generate_group()
            group.headman = random.choice(students)
            group.curator = random.choice(teachers)
            group.save()
