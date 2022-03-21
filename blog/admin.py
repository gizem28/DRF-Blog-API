
from django.contrib import admin
from .models import Blog
from .models import Comment, Like, BlogView

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(BlogView)