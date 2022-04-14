# Generated by Django 4.0.4 on 2022-04-14 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=10000, unique=True)),
                ('uuid', models.CharField(max_length=15, unique=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
