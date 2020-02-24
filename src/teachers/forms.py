from django.forms import ModelForm, ValidationError

from teachers.models import Teacher


class BaseTeacherForm(ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        email_exists = Teacher.objects\
            .filter(email__iexact=email)\
            .exclude(email__iexact=self.instance.email)\
            .exists()
        if email_exists:
            raise ValidationError(f'{email} is already used!')
        return email

    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        telephone_exists = Teacher.objects \
            .filter(telephone__iexact=telephone) \
            .exclude(telephone__iexact=self.instance.telephone) \
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


class TeacherAddForm(BaseTeacherForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherAdminForm(BaseTeacherForm):
    class Meta:
        model = Teacher
        fields = ('id', 'email', 'first_name', 'last_name', 'telephone')
