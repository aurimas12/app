from django.contrib import admin
from api.posts.models import Post, Tags, Description


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['language']
    search_fields = ['language']


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ['text']
    search_fields = ['text']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('register_id', 'post_url', 'position', 'salary_min', 'salary_max', 'company', 'tags', 'download_datetime')
    search_fields = ('register_id', 'salary_min', 'salary_max', 'position', 'tags', 'company', 'download_datetime',) 
    fields = ('register_id', 'post_url', 'position', 'salary_min', 'salary_max', 'company', 'tags')


