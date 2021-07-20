from django.urls import path
from store import views

app_name = "store"
urlpatterns = [
    path("", views.store, name="store"),
    # path("sign-in/", UserSignInView.as_view(), name="sign-in"),
    # path("logout/", UserLogoutView.as_view(), name="logout"),
    # path("profile/", UserProfileView.as_view(), name="profile"),
]
