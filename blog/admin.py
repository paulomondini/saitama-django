from django.contrib import admin

from .models import Category, Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'posted_at']
    list_filter = ['categories']
    search_fields = ['title', 'content']
    filter_horizontal = ['categories']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'posted_at']
    list_filter = ['post']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
