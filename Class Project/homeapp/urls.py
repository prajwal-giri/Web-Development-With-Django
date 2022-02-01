from django.urls import path
from .views import HomePageView, Test

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("test/", Test.as_view(), name="test1")
]
