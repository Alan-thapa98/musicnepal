# Generated by Django 3.1.2 on 2021-07-03 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musiclist', '0004_auto_20210703_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='lastname',
        ),
    ]