# Generated by Django 4.0.4 on 2022-07-26 03:21

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
