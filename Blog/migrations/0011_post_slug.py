# Generated by Django 3.0.3 on 2020-05-14 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0010_auto_20200513_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
