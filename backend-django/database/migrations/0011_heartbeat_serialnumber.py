# Generated by Django 2.2.4 on 2021-06-06 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_auto_20210606_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='heartbeat',
            name='serialNumber',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
