from django.contrib import admin
from .models import Post, Comment, Category

for i in [Post, Comment, Category]:
    admin.site.register(i)