# Generated by Django 4.1.3 on 2022-11-04 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_userproject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userproject',
            old_name='roll',
            new_name='role',
        ),
    ]
