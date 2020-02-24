from django.db.models.signals import pre_save
from django.dispatch import receiver
from students.models import Student


@receiver(pre_save, sender=Student)
def pre_save_student(sender, instance, **kwargs):
    instance.first_name = instance.first_name.strip().lower().capitalize()
    instance.last_name = instance.last_name.strip().lower().capitalize()
    instance.email = instance.email.lower()
    instance.telephone = ''.join(i for i in instance.telephone if i.isdigit())
    if instance.id is None:
        print('Object is created!')
