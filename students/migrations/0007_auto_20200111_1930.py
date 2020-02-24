# Generated by Django 3.0.2 on 2020-01-11 19:30

from django.db import migrations


def forward(apps, schema_editor):
    Student = apps.get_model('students', 'Student')
    for student in Student.objects.all().only('id', 'telephone').iterator():
        student.telephone = ''.join(x for x in student.telephone if x.isdigit())
        student.save(update_fields=['telephone'])


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20200108_1945'),
    ]

    operations = [
        migrations.RunPython(forward),
    ]