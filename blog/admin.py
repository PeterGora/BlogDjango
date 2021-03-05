from django.contrib import admin
from .models import Category, Post, Comment

class CategoryAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'pub_date', 'content', 'created_by', 'category')
    list_filter = ['post_title', 'pub_date', 'content', 'created_by', 'category']
    date_hierarchy = 'pub_date'
    search_fields = ['post_title', 'created_by', 'pub_date']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'pub_date', 'created_by', 'accepted')
    list_filter = ['post', 'pub_date', 'created_by', 'accepted']
    date_hierarchy = 'pub_date'
    search_fields = ['created_by', 'pub_date']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
