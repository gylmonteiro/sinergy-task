# Generated by Django 5.0.4 on 2024-05-17 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_tasks', '0005_alter_task_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='volunteers',
            new_name='volunteers_involved',
        ),
    ]
