from django.shortcuts import render


from .models import Cblog
from homepage.models import HomePage

# Create your views here.


def fblog(request):
    context = {
        "result1": Cblog.objects.all(),
        "result": HomePage.objects.first()



    }
    return render(request, "blogpage/blog.html", context)


def detail(request, blog_id):
    context = {
        'result3': Cblog.objects.get(id=blog_id),
        "result": HomePage.objects.first()
    }
    return render(request, 'blogpage/blog_detail.html', context)
