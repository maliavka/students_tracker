
from django.db import models
from faker import Faker


class Teacher(models.Model):
    teach_name = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=20, blank=True, default=None)
    last_name = models.CharField(max_length=20, blank=True, default=None)
    birth_date = models.DateField(null=True, blank=True, default=None)
    position = models.CharField(max_length=50, blank=True, default=None)
    email = models.EmailField()
    # add avatar TODO
    telephone = models.CharField(max_length=30, blank=True, default=None)  # clean phone TODO

    def get_info(self):
        return f'{self.first_name} ' \
               f'{self.last_name}: ' \
               f'{self.email}, ' \
               f'{self.birth_date}'

    @classmethod
    def generate_teacher(cls):
        fake = Faker()
        teacher = cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birth_date=fake.date_of_birth(
                tzinfo=None,
                minimum_age=25,
                maximum_age=65
            ),
            position=fake.job(),
            email=fake.email(),
            telephone=fake.phone_number(),
        )
        teacher.save()
        return teacher
