# Generated by Django 2.1 on 2018-11-23 00:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('description', models.TextField(blank=True, default='', max_length=5000, null=True)),
                ('achievement', models.TextField(blank=True, default='', max_length=5000, null=True)),
            ],
        ),
    ]
