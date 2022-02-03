from django.shortcuts import render
from .models import Cblog
from homepage.models import HeaderNav, FooterNav

# Create your views here.


def fblog(request):
    context = {
        "result": HeaderNav.objects.all(),
        "result1": FooterNav.objects.all(),
        "result6": Cblog.objects.all(),

    }
    return render(request, "blogpage/blog.html", context)
