from django.contrib .auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate,  login, logout
from django.db.models import Case, When
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

# these is soptify impornt
from django.http import JsonResponse
# Create your views here.
from .models import *


def base(request, channel):
    song = list(Song.objects.all())
    chan = Channel.objects.filter(name=channel).first()
    video_ids = str(chan.music).split(" ")[1:]
    newsongs = Song.objects.order_by('-song_id',)[0:10]
    preseved = Case(*[When(pk=pk, then=pos)
                      for pos, pk in enumerate(video_ids)])
    song = Song.objects.filter(song_id__in=video_ids).order_by(preseved)
    context = {'chan': chan, 'song': song, 'newsongs': newsongs, }
    return render(request, 'base.html', context)


def browse(request):
    top_10_music = Song.objects.all()[0:12]
    top_10_singer = Artist.objects.all()[0:12]
    top_10_views = Song.objects.order_by('views',)[0:12]
    top_10_date = Song.objects.order_by('-update',)[0:12]
    to_10_cats = Category.objects.all()[0:12]
    newsongs = Song.objects.order_by('-song_id',)[0:10]
    context = {"top_10_music": top_10_music, "top_10_singer": top_10_singer, "top_10_views": top_10_views,
               "top_10_date": top_10_date, "to_10_cats": to_10_cats, "newsongs": newsongs}
    return render(request, 'browse.html', context)

# these is the features section


def new_song(request):
    new_song = Song.objects.order_by('-updated')[0:30]
    context = {'new_song': new_song}
    return render(request, 'new_song.html', context)


def old_song(request):
    old_song = Song.objects.order_by('updated')[0:30]
    context = {'old_song': old_song}
    return render(request, 'old_song.html', context)


def most_listened(request):
    most_listened = Song.objects.order_by('views')[0:30]
    context = {'most_listened': most_listened}
    return render(request, 'most_listened.html', context)


def artists(request):
    newsongs = Song.objects.order_by('-song_id',)[0:10]
    artists = Artist.objects.all()
    context = {'artists': artists, 'newsongs': newsongs}
    return render(request, 'artists.html', context)


def artist(request, artist):
    query = str(artist)
    title = Song.objects.filter(name__icontains=query)  # song
    Allsongsartist = Song.objects.filter(
        singer__icontains=query)  # Allsongsartist_singer
    Allsongstags = Song.objects.filter(tags__icontains=query)
    AllsongsMovie = Song.objects.filter(movie__icontains=query)
    Allsongs = title.union(
        Allsongstags, Allsongsartist, AllsongsMovie)
    print(Allsongs)
    # Artists
    artist_songs = Artist.objects.filter(name__icontains=query)
    newsongs = Song.objects.order_by('-song_id',)[0:10]
    context = {'query': query, 'Allsongs': Allsongs,
               'artist_songs': artist_songs, 'newsongs': newsongs}
    return render(request, 'artist.html', context)


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        Allsongs = Song.objects.none()
    else:
        title = Song.objects.filter(name__icontains=query)  # song
        Allsongsartist = Song.objects.filter(
            singer__icontains=query)  # Allsongsartist_singer
        Allsongstags = Song.objects.filter(tags__icontains=query)
        AllsongsMovie = Song.objects.filter(movie__icontains=query)
        Allsongs = title.union(
            Allsongstags, Allsongsartist, AllsongsMovie)
    # Artists
    artist = Artist.objects.filter(name__icontains=query)
    newsongs = Song.objects.order_by('-song_id',)[0:10]
    params = {'Allsongs': Allsongs, 'query': query,
              'artist': artist, 'newsongs': newsongs}
    return render(request, 'search.html', params)


def history(request):
    # these is the logic for the saving history
    if request.method == "POST":
        user = request.user
        music_id = request.POST['music_id']

        history = History.objects.filter(user=user)
        for i in history:
            if music_id == i.music_id:
                return redirect(f"/musiclist/songs/{music_id}")
        else:
            history = History(user=user, music_id=music_id)
            history.save()
            song = Song.objects.filter(song_id=music_id).first()
            context1 = {
                'song': song,
            }
            return redirect(f"/musiclist/songs/{music_id}")
    history = History.objects.filter(user=request.user)
    ids = []
    for i in history:
        ids.append(i.music_id)
    preseved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preseved)
    context = {
        'song': song
    }
    return render(request, 'history.html', context)


def watchlater(request):
    newsongs = Song.objects.order_by('-song_id',)[0:10]
    # these is the logic for the saving watchlater
    if request.method == "POST":
        user = request.user
        video_id = request.POST['video_id']

        watch = Watchlater.objects.filter(user=user)
        for i in watch:
            if video_id == i.video_id:
                msg = "your video is already Added"
                return redirect(f"/musiclist/songs/{video_id}")
        else:
            watchlater = Watchlater(user=user, video_id=video_id)
            watchlater.save()
            msg = "your video is  Added for watch latter."
            song = Song.objects.filter(song_id=video_id).first()
            context1 = {
                'song': song,
                'msg': msg
            }
            return redirect(f"/musiclist/songs/{video_id}", context1)
    wl = Watchlater.objects.filter(user=request.user)
    ids = []
    for i in wl:
        ids.append(i.video_id)
    preseved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preseved)
    context2 = {
        'song': song,
        'newsongs': newsongs,
    }
    return render(request, 'favourite.html', context2)


def upload(request):

    if request.method == "POST":
        # Get the post parameters
        name = request.POST['name']
        singer = request.POST['singer']
        category = request.POST['category']
        tags = request.POST['tags']
        album_name = request.POST['album_name']
        imgofsong = request.FILES['imgofsong']
        movie = request.POST['movie']
        song = request.FILES['file']
        update = request.POST['update']

        song_model = Song(name=name, singer=singer, category=category, tags=tags, album_name=album_name,
                          imgofsong=imgofsong, song=song, movie=movie, update=update,)
        song_model.save()

        music_id = song_model.song_id
        channel_find = Channel.objects.filter(name=str(request.user))

        for i in channel_find:
            i.music += f" {music_id}"
            i.save()
        # Create the user
    cats = Category.objects.all()
    #     catvalues = Category.objects.values("id", "image", "title")
    #     print(catvalues)
    context = {"cats": cats, }
    return render(request, 'upload.html', context)


def channel(request, channel):
    chan = Channel.objects.filter(name=channel).first()
    video_ids = str(chan.music).split(" ")[1:]
    newsongs = Song.objects.order_by('-song_id',)[0:10]
    preseved = Case(*[When(pk=pk, then=pos)
                      for pos, pk in enumerate(video_ids)])
    song = Song.objects.filter(song_id__in=video_ids).order_by(preseved)
    context = {'chan': chan, 'song': song, 'newsongs': newsongs, }
    return render(request, 'channel.html', context)


def albums(request):
    chan = Channel.objects.all()
    cats = Category.objects.all()
    newsongs = Song.objects.order_by('-song_id',)[0:10]
    context = {'cats': cats, 'chan': chan, 'newsongs': newsongs, }
    return render(request, 'albums.html', context)


def discover(request):
    discoverys = Category.objects.all()
    newsongs = Song.objects.order_by('-song_id',)[0:10]
    context = {'discoverys': discoverys, 'newsongs': newsongs, }
    return render(request, "discoverys.html", context)


def categorys(request, category):
    newsongs = Song.objects.order_by('-song_id',)[0:10]
    query = str(category)
    allsongcatsTitle = Song.objects.filter(name__icontains=query)
    allsongcatsinger = Song.objects.filter(singer__icontains=query)
    allsongcatstags = Song.objects.filter(tags__icontains=query)
    allsongcatstags = Song.objects.filter(category__icontains=query)
    allsongcatsMovie = Song.objects.filter(movie__icontains=query)
    allsongcats = allsongcatsTitle.union(
        allsongcatstags, allsongcatsinger, allsongcatsMovie)
    context = {'allsongcats': allsongcats, 'newsongs': newsongs, }
    return render(request, 'categorys.html', context)


def login(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        from django.contrib.auth import login
        login(request, user)
        return redirect('/')
    return render(request, 'login.html')


def singup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        user = authenticate(username=username, password=pass1)
        from django.contrib.auth import login
        login(request, user)

        channel = Channel(name=username)
        channel.save()

        return redirect('/')
    return render(request, 'singup.html')


def handelLogout(request):
    logout(request)
    return redirect('/')


def about(request):
    newsongs = Song.objects.order_by('-song_id',)[0:10]
    context = {'newsongs': newsongs, }
    return render(request, 'about.html', context)
