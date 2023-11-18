from django.contrib import admin
from .models import Post, Tags, Description


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('register_id', 'post_url', 'position', 'salary_min', 'salary_max', 'company',)
    search_fields = ('register_id', 'salary_min', 'salary_max', 'position', 'publish_date') 


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['language']
    search_fields = ['language']


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ['text']
    search_fields = ['text']

