from django.contrib .auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate,  login, logout
from django.db.models import Case, When
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

# these is soptify impornt
from django.http import JsonResponse
# Create your views here.
from musiclist.models import *


def index(request):
    song = Song.objects.all()
    music_list = list(Song.objects.all().values())
    newsongs = Song.objects.order_by('-song_id',)[0:10]
    return render(request, 'index.html', {'song': song, 'newsongs': newsongs,'music_list':music_list,})
