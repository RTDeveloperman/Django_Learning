from django.urls import path
from blog.views import home,api,article_detais
app_name="blog"
urlpatterns = [
    path('', home, name="home"),
    path('api', api, name="api"),
    path('article/<slug:slug>', article_detais, name="article_detais_url"),
]
