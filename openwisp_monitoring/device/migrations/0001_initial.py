# Generated by Django 2.0.2 on 2018-02-26 12:01

import swapper
from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('config', '0012_auto_20180219_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceData',
            fields=[],
            options={
                'indexes': [],
                'proxy': True,
                'swappable': swapper.swappable_setting(
                    'device_monitoring', 'DeviceData'
                ),
            },
            bases=(swapper.get_model_name('config', 'Device'),),
        ),
    ]
