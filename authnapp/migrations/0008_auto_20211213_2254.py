# Generated by Django 2.2.24 on 2021-12-13 22:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0007_auto_20211212_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 15, 22, 54, 5, 54799, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
