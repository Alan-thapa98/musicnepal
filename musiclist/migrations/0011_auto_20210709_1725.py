# Generated by Django 3.1.2 on 2021-07-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiclist', '0010_auto_20210709_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='update',
            field=models.IntegerField(default=1),
        ),
    ]
