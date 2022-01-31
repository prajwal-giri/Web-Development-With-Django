from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = "homefolder/home.html"

class Test(TemplateView):
    template_name = "test.html"