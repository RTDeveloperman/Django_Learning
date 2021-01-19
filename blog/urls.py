from django.urls import path
from blog.views import home,api,article_detais,category_list
app_name="blog"
urlpatterns = [
    path('', home, name="home"),
    path('api', api, name="api"),
    path('article/<slug:slug>', article_detais, name="article_detais_url"),
    path('category/<slug:slug>', category_list, name="category_list_url"),
    path('page/<int:page>', home, name="home"),
    #path('category/<slug:slug>', article_detais, name="category_list_url"),
]
