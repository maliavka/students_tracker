# Generated by Django 3.0.2 on 2020-02-10 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_auto_20200204_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
