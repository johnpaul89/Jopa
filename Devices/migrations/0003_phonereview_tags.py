# Generated by Django 2.1.3 on 2018-11-25 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Devices', '0002_auto_20181125_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonereview',
            name='tags',
            field=models.ManyToManyField(to='Devices.tags'),
        ),
    ]