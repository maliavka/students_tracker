from datetime import datetime
from django.db import models
from faker import Faker

'''
CREATE TABLE students_STUDENT(
first_name varchar(20)
);
'''


class Student(models.Model):
    # GRADE_CHOICES = (
    #     ('1', 'FreshMan'),
    #     ('2', 'Senior'),
    # )
    # grade = models.PositiveSmallIntegerField(choices=GRADE_CHOICES)
    st_name = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True, default=None)
    email = models.EmailField(unique=True)
    # add avatar TODO
    telephone = models.CharField(unique=True, max_length=40, blank=True, default=None)
    address = models.CharField(max_length=225, null=True, blank=True)
    st_group = models.ForeignKey('students.Group', null=True, blank=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # pre_save
        # self.email = self.email.lower()
        super().save(*args, **kwargs)
        # post_save

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

    def __str__(self):
        return f'{self.id} {self.full_name} {self.st_group} '

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Group(models.Model):
    group_name = models.CharField(max_length=128, null=True, blank=True)
    # curator = models.CharField(max_length=25, null=True, blank=True)

    curator = models.ForeignKey('teachers.Teacher', null=True, blank=True, on_delete=models.CASCADE)
    headman = models.ForeignKey('students.Student', null=True, blank=True, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True, default=None)

    def get_info_group(self):
        return f'{self.group_name}: {self.curator}, {self.headman}, {self.start_date}'

    @classmethod
    def generate_group(cls):
        fake = Faker()
        group = cls(
            # group_number=fake.random_int(min=100, max=999, step=1),
            # curator=fake.name(),
            # headman=fake.name(),
            start_date=fake.date(pattern="%Y-%m-%d", end_datetime=None),
        )
        group.save()
        return group

    def __str__(self):
        return f'Group {self.group_name} '


from students.signals import *
