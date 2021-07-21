from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user.forms import UserRegisterForm


class UserRegisterView(CreateView):
    """User sign-up view implementation"""

    form_class = UserRegisterForm
    template_name = "user/register.html"
    success_url = reverse_lazy("user:login")


class UserLoginView(LoginView):
    """User sign-in view implementation"""

    template_name = "user/login.html"


class UserLogoutView(LogoutView):
    """User logout view implementation"""

    pass
