from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.shortcuts import reverse
# from .utils import get_random_code
from django.template.defaultfilters import slugify
from django.db.models import Q

# these is for the music length
from .helper import get_audio_length
from .validators import validate_is_audio


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cat_imgs/")
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

# these is the backup plan for the modleis the rest oof the plan don't work


class Artist (models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="artist_img/")
    bio = models.TextField(max_length=2000)
    bg_imgs = models.ImageField(default='bg.jpg', upload_to='bg_img/')
    views = models.IntegerField(default=0)
    update = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90000)
    singer = models.CharField(max_length=90000)
    category = models.CharField(max_length=90000, default="")
    tags = models.CharField(max_length=90000)
    album_name = models.CharField(max_length=90000)
    time_length = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True)
    song = models.FileField(upload_to='musics/',
                            validators=[validate_is_audio])
    imgofsong = models.ImageField(upload_to='imgofsong', default="0")
    movie = models.CharField(max_length=90000, default="")
    views = models.IntegerField(default=0)
    update = models.IntegerField(default=1)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.time_length:
            # logic for getting length of audio
            audio_length = get_audio_length(self.song)
            self.time_length = f'{audio_length:.2f}'

        return super().save(*args, **kwargs)

    class META:
        ordering = "id"

    def __str__(self):
        return f'{self.name}-{self.time_length}'


class Channel(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    lastname = models.CharField(max_length=2000)
    bio = models.TextField(max_length=2000)
    # thses is vary imporant to check which person uploaded the  muisc
    music = models.CharField(max_length=90000000)
    # end of  vary imporant to check which person uploaded the  muisc
    imgofablum = models.ImageField(default='user.png', upload_to='imgofablum')
    bgimgofalbum = models.ImageField(default='bg.jpg', upload_to='bg_img/')
    #  upload_to='bgimg/')
    views = models.IntegerField(default=0)
    update = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    watch_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=200000, default="")
    views = models.IntegerField(default=0)
    update = models.DateTimeField(blank=True)

    def __str__(self):
        return f" {self.user} - added music for the watchlater."


class Listenlater(models.Model):
    watch_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=200000, default="")
    update = models.DateTimeField(blank=True)

    def __str__(self):
        return f" {self.user} - added music for the watchlater."


# class History(models.Model):
#     history_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     music_id = models.CharField(max_length=200000, default="")

#     def __str__(self):
#         return f" {self.user} - added music for the history."
