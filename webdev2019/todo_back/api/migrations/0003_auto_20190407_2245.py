# Generated by Django 2.2 on 2019-04-07 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190407_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 7, 22, 45, 29, 645795)),
        ),
    ]