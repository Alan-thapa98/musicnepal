# Generated by Django 3.1.2 on 2021-06-11 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='cat_imgs/')),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('lastname', models.CharField(max_length=2000)),
                ('bio', models.TextField(max_length=2000)),
                ('music', models.CharField(max_length=90000000)),
                ('imgofablum', models.ImageField(default='1', upload_to='imgofablum')),
                ('bgimgofalbum', models.ImageField(default='user.png', upload_to='')),
                ('views', models.IntegerField(default=0)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('singerid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('lastname', models.CharField(max_length=2000)),
                ('bio', models.TextField(max_length=2000)),
                ('image', models.ImageField(upload_to='singer_imgs/')),
                ('bgimgofalbum', models.ImageField(default='user.png', upload_to='')),
                ('likes', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('music', models.CharField(max_length=90000000)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200000)),
                ('singer', models.CharField(max_length=200000)),
                ('category', models.CharField(default='', max_length=200000)),
                ('tags', models.CharField(max_length=200000)),
                ('imgofsong', models.ImageField(default='0', upload_to='imgofsong')),
                ('song', models.FileField(max_length=100000000000, upload_to='songs')),
                ('movie', models.CharField(default='', max_length=200000)),
                ('credit', models.CharField(default='', max_length=200000)),
                ('views', models.IntegerField(default=0)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='lsitenlater',
            fields=[
                ('watch_id', models.AutoField(primary_key=True, serialize=False)),
                ('video_id', models.CharField(default='', max_length=200000)),
                ('update', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='favourite',
            fields=[
                ('watch_id', models.AutoField(primary_key=True, serialize=False)),
                ('video_id', models.CharField(default='', max_length=200000)),
                ('update', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
