# Generated by Django 3.0.3 on 2020-05-13 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_remove_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
