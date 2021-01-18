from django.shortcuts import render,get_object_or_404
from    django.http import HttpResponse,JsonResponse
from .models import article,Category
            #def home(request):
            #    return HttpResponse("Hello world!")

#def home(request):
#    context={
#        "username":"reza",
#        "age":32,
#        "job":"developer",
#    }
#    return render(request, "home.html",context)
def home(request):
    context={
        "article": article.objects.published_article(), #"article":article.objects.all().filter(status="p"),# - nozoli
    }
    return render(request, "index.html",context)

def article_detais(request,slug):
    context={
        'article': get_object_or_404(article.objects.published_article(), slug=slug), # 'article':get_object_or_404(article,slug=slug,status="p"),

    }
    return render(request,'post.html',context)

def category_list(request,slug):
    context={
        "category":get_object_or_404(Category,slug=slug,status=True),
    }
    return  render(request,'category.html',context)

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
