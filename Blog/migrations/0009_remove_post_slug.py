# Generated by Django 3.0.3 on 2020-05-13 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_auto_20200513_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
