# Generated by Django 3.2.9 on 2021-11-21 13:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0003_rename_job_seekers_job_seeker'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Job_seeker',
            new_name='Job_seekers',
        ),
    ]
