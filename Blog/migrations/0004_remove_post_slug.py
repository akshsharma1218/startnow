# Generated by Django 3.0.3 on 2020-05-13 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_auto_20200513_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
