# Generated by Django 3.0.2 on 2020-02-04 22:27

from django.db import migrations


def forward(apps, schema_editor):
    Teacher = apps.get_model('teachers', 'Teacher')
    for teacher in Teacher.objects.all().only('id', 'telephone').iterator():
        teacher.telephone = ''.join(
            x for x in teacher.telephone if x.isdigit()
        )
        teacher.save(update_fields=['telephone'])


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_auto_20200201_2216'),
    ]

    operations = [
        migrations.RunPython(forward),
    ]