# Generated by Django 4.2.3 on 2023-08-05 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problems',
            name='input',
        ),
    ]