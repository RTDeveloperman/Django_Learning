from django.urls import path
from blog.views import api,article_detais,category_list,ArticleList,ArticleDetails,CategoryList,AuthorList
app_name="blog"
urlpatterns = [
    path('', ArticleList.as_view(), name="home"),
    path('page/<int:page>', ArticleList.as_view(), name="home"),

    path('api', api, name="api"),

    path('article/<slug:slug>', ArticleDetails.as_view(), name="article_detais_url"),

    path('category/<slug:slug>', CategoryList.as_view(), name="category_list_url"),
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name="category_list_url"),

    path('author/<slug:username>', AuthorList.as_view(), name="author_list_url"),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name="author_list_url"),

]
