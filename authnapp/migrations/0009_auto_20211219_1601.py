# Generated by Django 2.2.24 on 2021-12-19 16:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0008_auto_20211213_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 21, 16, 1, 57, 967586, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
