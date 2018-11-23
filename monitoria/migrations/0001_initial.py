# Generated by Django 2.1 on 2018-11-23 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('date', models.DateTimeField(blank=True)),
                ('image', models.ImageField(blank=True, max_length=30, upload_to='')),
                ('content', models.CharField(blank=True, max_length=30)),
                ('max_mentorado', models.IntegerField(default=4)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
