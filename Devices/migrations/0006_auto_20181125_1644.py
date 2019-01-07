# Generated by Django 2.1.3 on 2018-11-25 16:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Devices', '0005_auto_20181125_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonereview',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='reviewlikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='phonespecs',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='specslikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
