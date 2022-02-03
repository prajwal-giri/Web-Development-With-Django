from django.urls import path
from .views import fblog


urlpatterns = [
    path("blog/", fblog, name="blog1")
]
