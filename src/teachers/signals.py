from django.db.models.signals import pre_save
from django.dispatch import receiver
from teachers.models import Teacher


@receiver(pre_save, sender=Teacher)
def pre_save_student(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()
    instance.email = instance.email.lower()
    instance.telephone = ''.join(i for i in instance.telephone if i.isdigit())
    if instance.id is None:
        print('Object is created!')