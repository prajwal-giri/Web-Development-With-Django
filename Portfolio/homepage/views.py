from django.shortcuts import render
from .models import HomePage
# Create your views here.


def home_page(request):
    context = {
        "result": HomePage.objects.first(),

    }
    return render(request, "homepage/home.html", context)
