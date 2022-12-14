# Generated by Django 4.1.3 on 2022-11-04 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_userexperience'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll', models.CharField(max_length=100)),
                ('releaseDate', models.CharField(max_length=100)),
                ('responsibilities', models.CharField(max_length=300)),
                ('basedOn', models.CharField(max_length=100)),
                ('projectImage', models.ImageField(upload_to='Project-Photos')),
                ('projectLink', models.CharField(max_length=100)),
                ('belongsTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
