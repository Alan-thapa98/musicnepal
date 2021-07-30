from django.urls import path
from . import views
urlpatterns = [
    path('base/<str:channel>', views.base, name='base'),
    path('search', views.search, name='search'),
    path('artists', views.artists, name='artists'),
    path('artist/<str:artist>', views.artist, name='artist'),
    path('about', views.about, name='about'),
    # these is the browse url
    path('browse', views.browse, name='browse'),
    path('new_song', views.new_song, name='new_song'),
    path('old_song', views.old_song, name='old_song'),
    path('most_listened', views.most_listened, name='most_listened'),
    # path('history', views.history, name='history'),
    path('watchlater', views.watchlater, name='watchlater'),
    path('c/<str:channel>', views.channel, name='channel'),
    path('discover', views.discover, name="discover"),
    path('albums/', views.albums, name='albums'),
    path('cats/<str:category>', views.categorys, name='categorys'),
    path('upload', views.upload, name="upload"),
    # authandications
    path('login', views.login, name='login'),
    path('singup', views.singup, name='singup'),
    path('logout', views.handelLogout, name="handleLogout"),

]
