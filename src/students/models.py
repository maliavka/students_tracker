import random

from datetime import datetime
from django.db import models
from faker import Faker


'''
CREATE TABLE students_STUDENT(
first_name varchar(20)
);
'''
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()
    # add avatar TODO
    telephone = models.CharField(max_length=16)  # clean phone TODO
    address = models.CharField(max_length=225, null=True, blank=True)

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
    group_name = models.CharField(max_length=25)
    faculty_name = models.CharField(max_length=25)
    course_name = models.IntegerField()
    start_date = models.DateField()