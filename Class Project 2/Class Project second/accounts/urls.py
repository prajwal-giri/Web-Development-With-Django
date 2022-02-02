from django.urls import path
from .views import SignUpView, change_password, password_reset
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path("password_change/", change_password, name="password_change"),
    # path("password_change/done/", PasswordChangeDone.as_view(),
    #      name="password_change_done"),
    path("password_reset/", password_reset, name="password_reset1"),
    # path("password_reset/done/", PasswordResetDone.as_view(),
    #      name="reset_email_sent"),
    # path("reset/NA/set-password/", PasswordChangeView)
]
