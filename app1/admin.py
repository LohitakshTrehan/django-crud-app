from django.contrib import admin

# Register your models here.

from app1.models import *
admin.site.register(Artist)
admin.site.register(Album)
