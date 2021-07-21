from django.contrib.auth import views as auth_views
from django.urls import path
from user.views import UserLoginView, UserRegisterView

app_name = 'user'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
