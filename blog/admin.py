from django.contrib import admin
from .models import *
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'jpublish_time',
        'status',
        'description',

    )
    search_fields = (
        'title',
        'slug',
        'description',
        'status',
    )
    list_filter = (
        'publish_time',
        'status',
    )
    prepopulated_fields = {'slug':('title',)}
    ordering = ['status']#  . be manaye nozoli
admin.site.register(article,ArticleAdmin)
