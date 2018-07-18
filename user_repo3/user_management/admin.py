from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Preferences)
admin.site.register(Favourites)
# admin.site.register(Profile)