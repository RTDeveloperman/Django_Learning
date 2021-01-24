from django.urls import path
from blog.views import api,article_detais,category_list,ArticleList,ArticleDetails
app_name="blog"
urlpatterns = [
   # path('', home, name="home"),
    path('', ArticleList.as_view(), name="home"),
    path('api', api, name="api"),
   # path('article/<slug:slug>', article_detais, name="article_detais_url"),
    path('article/<slug:slug>', ArticleDetails.as_view(), name="article_detais_url"),
    path('category/<slug:slug>', category_list, name="category_list_url"),
    path('category/<slug:slug>/page/<int:page>', category_list, name="category_list_url"),
   #path('page/<int:page>', home, name="home"),
    path('page/<int:page>', ArticleList.as_view(), name="home"),
    #path('category/<slug:slug>', article_detais, name="category_list_url"),
]
