from django.forms import ModelForm, Form, EmailField, CharField, ValidationError
from django.core.mail import send_mail
from django.conf import settings

from students.tasks import send_email_async

from students.models import Student, Group


class BaseStudentForm(ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        email_exists = Student.objects\
            .filter(email__iexact=email)\
            .exclude(email__iexact=self.instance.email)\
            .exists()
        if email_exists:
            raise ValidationError(f'{email} is already used!')
        return email

    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        telephone_exists = Student.objects \
            .filter(telephone__iexact=telephone) \
            .exclude(id=self.instance.id) \
            .exists()
        if telephone_exists:
            raise ValidationError(f'{telephone} is already used!')
        telephone = ''.join(i for i in telephone if i.isdigit())
        return telephone

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].capitalize()
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].capitalize()
        return last_name


class StudentAddForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAdminForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = ('id', 'email', 'first_name', 'last_name', 'telephone')


class GroupAddForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class ContactForm(Form):
    email = EmailField()
    subject = CharField()
    text = CharField()

    def save(self):
        data = self.cleaned_data
        subject = data['subject']
        message = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER, ]
        student = Student.objects.get_or_create(email=email_from)[0]
        # student = Student.objects.create(email=email_from)
        # send_mail(subject, message, email_from, recipient_list)
        send_email_async.delay(subject, message, recipient_list, student.id)
