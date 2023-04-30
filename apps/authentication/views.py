from typing import Any
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse

from apps.authentication.forms import MyAuthenticationForm


User = get_user_model()


class MyLoginView(LoginView):
    template_name = "authentication/login.html"
    redirect_authenticated_user = True
    form_class = MyAuthenticationForm

class MyLogoutView(LogoutView):
    template_name = "authentication/logout.html"
