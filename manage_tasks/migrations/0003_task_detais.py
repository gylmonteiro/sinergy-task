# Generated by Django 5.0.4 on 2024-04-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_tasks', '0002_task_prevision_hours_alter_task_expected_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='detais',
            field=models.TextField(blank=True, null=True),
        ),
    ]