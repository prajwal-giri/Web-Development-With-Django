from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page_view(request):
    return HttpResponse("Hello World")


def about_page_view(request):
    return HttpResponse("Hello From About Page")


def contact_page_view(request):
    return HttpResponse("<h1>Hello from contact page</h1> ")
