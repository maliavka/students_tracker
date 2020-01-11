from django.forms import ModelForm

from teachers.models import Teacher


class TeacherAddForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
