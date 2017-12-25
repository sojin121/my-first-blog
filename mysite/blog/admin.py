from django.contrib import admin
from .models import Post
from blog.models import GuessNumbers


admin.site.register(Post)
admin.site.register(GuessNumbers)