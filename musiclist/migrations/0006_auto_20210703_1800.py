# Generated by Django 3.1.2 on 2021-07-03 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiclist', '0005_remove_channel_lastname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='lastname',
        ),
        migrations.AddField(
            model_name='channel',
            name='lastname',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
    ]
