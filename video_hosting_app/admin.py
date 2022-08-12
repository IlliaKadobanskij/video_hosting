from django.contrib import admin

from video_hosting_app.models import *

admin.site.register(Video)
admin.site.register(ContentGenre)
admin.site.register(ContentCategory)
admin.site.register(ContentPost)
admin.site.register(ContentStatistics)
admin.site.register(Channel)
admin.site.register(Playlist)
admin.site.register(PostComment)
