from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from user.models import Customer


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]
