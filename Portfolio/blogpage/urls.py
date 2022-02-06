from django.urls import path
from .views import fblog, detail


urlpatterns = [
    path("blog/", fblog, name="blog1"),
    path('blog/<int:blog_id>/', detail, name='blogdetail'),
]
