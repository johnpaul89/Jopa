# Generated by Django 2.1.3 on 2018-11-28 17:00

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Social', '0002_comment_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='post',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]