# Generated by Django 3.0.2 on 2020-01-25 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20200111_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='address',
        ),
    ]
