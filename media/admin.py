from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Comments)
admin.site.register(Post)
admin.site.register(Video)
admin.site.register(Song)
