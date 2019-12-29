from datetime import datetime
from django.db import models


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
        return f'{self.first_name}{self.last_name}{self.birth_date}'


    @classmethod
    def generate_student(cls):
        student = cls(
            first_name='D',
            last_name='K',
            birth_date=...,
            email='hfgydfgy@gmail.com',
            telephone='1234566',
        )
        student.save()