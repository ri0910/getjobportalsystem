# Generated by Django 3.2.9 on 2021-11-22 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='companyname',
            new_name='company',
        ),
    ]
