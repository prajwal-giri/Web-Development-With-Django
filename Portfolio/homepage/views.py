from django.shortcuts import render
from .models import HeaderNav, FooterNav, HeroHeadSection, HeroMiddleSection, HeroEndSection
# Create your views here.


def home_page(request):
    context = {
        "result": HeaderNav.objects.all(),
        "result1": FooterNav.objects.all(),
        "result3": HeroHeadSection.objects.all(),
        "result4": HeroMiddleSection.objects.all(),
        "result5": HeroEndSection.objects.all()

    }
    return render(request, "homepage/home.html", context)
