from django.contrib import admin

from myapp.models import CensorInfo, Actor, Director, MovieDb

# Register your models here.
admin.site.register(CensorInfo)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(MovieDb)
