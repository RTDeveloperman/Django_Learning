from django.contrib import admin
from .models import *
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'jpublish_time',
        'status',
        'short_description',
        'category_to_string',

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

    def category_to_string(self,obj):
        return ", ".join([category.title for category in obj.category.all()])
    category_to_string.short_description="دسته بندی"
admin.site.register(article,ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'position',
        'title',
        'slug',
        'status',
    )
    search_fields = (
        'title',
        'slug',
    )
    list_filter = (
       ['status']
    )
    prepopulated_fields = {'slug':('title',)}
admin.site.register(Category,CategoryAdmin)
