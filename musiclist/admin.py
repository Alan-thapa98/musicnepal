from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(Song)
admin.site.register(Channel)
admin.site.register(Favorite)
admin.site.register(Listenlater)
admin.site.register(Artist)
