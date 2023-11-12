from django.contrib import admin
from .models import Post, Tags, Description, Position


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('register_id', 'post_url', 'upload_post', 'salary', 'created_datetime', 'company',)
    search_fields = ('register_id', 'salary', 'upload_post', 'created_datetime',) 


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['language', 'post']
    search_fields = ['language']


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ['text', 'post']
    search_fields = ['text']


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['position', 'applicants_value']
    search_fields = ['position', 'applicants_value']
 