# Generated by Django 4.1.3 on 2022-11-04 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_usercertificate_issuedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercertificate',
            name='issueDate',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usercertificate',
            name='issuedBy',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usercertificate',
            name='link',
            field=models.CharField(max_length=100),
        ),
    ]
