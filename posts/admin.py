from django.contrib import admin

from posts.models import Post, Vote

admin.site.register(Post)
admin.site.register(Vote)

admin.site.site_header = 'Kelola Data Aplikasi'
admin.site.site_title = 'HQ'
admin.site.index_title = 'KobaApp'
