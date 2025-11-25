from django.contrib import admin
from .models import ForumGroup, Forum, Post

admin.site.register(ForumGroup)
admin.site.register(Forum)
admin.site.register(Post)
