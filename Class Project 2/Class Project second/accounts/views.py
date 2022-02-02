from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
# from django.views.generic import TemplateView


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def change_password(request):
    # success_url = reverse_lazy('password_change_done')
    return render(request, "registration/password_change_form.html")


# class PasswordChangeDone(TemplateView):
#     template_name = "registration/password_change_done.html"


def password_reset(request):
    # success_url = reverse_lazy('resent_email_sent')
    return render(request, "registration/password_reset_form.html")


# class PasswordResetDone(TemplateView):
#     template_name = "registration/password_reset_done.html"


# def password_reset_confrim(request):
#     return render(request, "registration/password_reset_confirm.html")
