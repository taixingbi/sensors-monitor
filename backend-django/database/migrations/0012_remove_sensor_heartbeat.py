# Generated by Django 2.2.4 on 2021-06-06 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_heartbeat_serialnumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='heartbeat',
        ),
    ]
