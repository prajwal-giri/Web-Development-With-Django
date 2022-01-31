from turtle import home
from django.urls import path
from .views import about_page_view, contact_page_view, home_page_view

urlpatterns = [
    path("", home_page_view, name="home"),
    path("about/", about_page_view, name="about"),
    path("contact/", contact_page_view, name="contact")
]
