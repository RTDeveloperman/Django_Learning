from django.contrib import admin
from .models import *

#Admin Header Change
admin.site.site_header="مدیریت وبلاگ جنگویی من"
#My Actions
def make_published(modeladmin, request, queryset):
    published=queryset.update(status='p')
    if(published==1):
        msg='منتشر شد'
    else:
        msg='منتشر شدند'
    modeladmin.message_user(request,"{}  مقاله  {}".format(published,msg))
make_published.short_description = "منتشر کردن"

def make_darft(modeladmin, request, queryset):
    draft=queryset.update(status='d')
    if(draft==1):
        msg='پیش نویس شد'
    else:
        msg='پیش نویس شدند'
    modeladmin.message_user(request,"{} مقاله {}".format(draft,msg))
make_darft.short_description = "پیش نویس"






class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'author',
        'jpublish_time',
        'status',
        'short_description',
        'category_to_string',
        'thumbnail_tag',

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
    actions = [make_published,make_darft]

    def category_to_string(self,obj):
        return ", ".join([category.title for category in obj.category.active_category()])
    category_to_string.short_description="دسته بندی"
admin.site.register(article,ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'position',
        'title',
        'slug',
        'status',
        'parent',
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
