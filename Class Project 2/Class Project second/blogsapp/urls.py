
from django.urls import path
from .views import fblog, detail, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path("blog/", fblog, name="blog1"),
    path('blog/<int:blog_id>/', detail, name='blogdetail'),
    path('blog/blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),

]
