from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import article
from django.views.generic import ListView
# Create your views here.


@login_required
def home(request):
    return render(request,"registration/home.html")

class ArticleList(LoginRequiredMixin,ListView):
    template_name = "registration/home.html"
    queryset =article.objects.all()