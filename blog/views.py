from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
from    django.http import HttpResponse,JsonResponse
from .models import article,Category
from django.contrib.auth.models import User
from django.views.generic import ListView,TemplateView,DetailView
            #def home(request):
            #    return HttpResponse("Hello world!")

#def home(request):
#    context={
#        "username":"reza",
#        "age":32,
#        "job":"developer",
#    }
#    return render(request, "home.html",context)
#def home(request,page=1):
#    articles_list=article.objects.published_article()
#    paginator=Paginator(articles_list,3)
#    #page=request.GET.get('page')
#    articles=paginator.get_page(page)
#    context={
#        "article": articles, #"article":article.objects.all().filter(status="p"),# - nozoli
#    }
#    return render(request, "index.html",context)
class ArticleList(ListView):
    #model = article
    template_name = "article_list.html"#dar sorat adam estefade bayad name index.html ra be article_list.html taghir dahim
    context_object_name = "article"#dar sorat adam estefade dar template bayad benevisim===>object_list
    queryset = article.objects.published_article()
    paginate_by = 6
def article_detais(request,slug):
    context={
        'article': get_object_or_404(article.objects.published_article(), slug=slug), # 'article':get_object_or_404(article,slug=slug,status="p"),

    }
    return render(request,'blog/post.html',context)
class ArticleDetails(DetailView):
    template_name = "blog/post.html"
    context_object_name="article"
    def get_object(self, queryset=None):
        slug=self.kwargs.get('slug')
        return get_object_or_404(article.objects.published_article(), slug=slug)

def category_list(request,slug,page=1):
    category=get_object_or_404(Category,slug=slug,status=True)
    articles_list = category.articles_rela.published_article()
    paginator = Paginator(articles_list, 3)
    articles = paginator.get_page(page)

    context={
        "category":category,
        "articles":articles,
    }
    return  render(request,'blog/category.html',context)
class CategoryList(ListView):
    template_name = "blog/category_list.html"
    paginate_by = 3
    def get_queryset(self):
        global category
        slug=self.kwargs.get("slug")
        category=get_object_or_404(Category.objects.active_category(), slug=slug, )
        return category.articles_rela.published_article()
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context["category"]=category
        return context

class AuthorList(ListView):
    template_name = "blog/author_list.html"
    paginate_by = 3
    def get_queryset(self):
        global author_category
        username=self.kwargs.get("username")
        author_category=get_object_or_404(User, username=username, )
        return author_category.article_author_rel.published_article()
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context["author_category"]=author_category
        return context
def api(request):
    data={
        "1":{
            "title":"مقاله ی چگونگی کسب و کار در جهان موازی",
            "id":20,
            "category":"حسابداری",
        },
        "2":{
            "title":"تکنولوژی های قدیمی",
            "id":28,
            "category":"کامپیوتر",
        },
        "3":{
            "title":"فوتبال پشمکی",
            "id":23,
            "category":"ورزشی",
        },
    }
    return JsonResponse(data)
