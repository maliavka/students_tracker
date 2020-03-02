from celery import shared_task
from django.core.mail import send_mail
from students.models import Student

# @shared_task
# def add(a, b):
#     print('ADD Works')
#     sleep(10)
#     print(a + b)
#     return a + b


@shared_task()
def send_email_async(subject, message, recipient_list, student_id):
    student_obj = Student.objects.get(id=student_id)
    send_mail(subject, message, student_obj.email, recipient_list, fail_silently=False)
