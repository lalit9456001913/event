# Generated by Django 3.0.2 on 2020-01-12 05:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_remove_event_event_dates'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
