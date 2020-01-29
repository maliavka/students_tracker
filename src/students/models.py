from datetime import datetime
from django.db import models
from faker import Faker

from teachers.models import Teacher


'''
CREATE TABLE students_STUDENT(
first_name varchar(20)
);
'''


class Student(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True, default=None)
    email = models.EmailField()
    # add avatar TODO
    telephone = models.CharField(max_length=30, null=True, blank=True)  # clean phone TODO
    address = models.CharField(max_length=225, null=True, blank=True)
    st_group = models.ForeignKey('students.Group', null=True, blank=True, on_delete=models.CASCADE)

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.birth_date}'

    @classmethod
    def generate_student(cls):
        fake = Faker()
        student = cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birth_date=datetime.now().date(),
            email=fake.email(),
            telephone=fake.phone_number(),
        )
        student.save()
        return student


class Group(models.Model):
    group_name = models.CharField(max_length=128, null=True, blank=True)
    curator = models.ForeignKey('teachers.Teacher', null=True, blank=True, on_delete=models.CASCADE)
    headman = models.ForeignKey('students.Student', null=True, blank=True, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True, default=None)

    def get_info_group(self):
        return f'{self.group_number}: {self.curator}, {self.start_date}'

    @classmethod
    def generate_group(cls):
        fake = Faker()
        group = cls(
            # group_number=fake.random_int(min=100, max=999, step=1),
            # curator=fake.name(),
            start_date=fake.date(pattern="%Y-%m-%d", end_datetime=None),
        )
        group.save()
        return group
