from django.urls import path
from store import views

app_name = "store"
urlpatterns = [
    path("", views.store, name="list"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    # path("logout/", UserLogoutView.as_view(), name="logout"),
    # path("profile/", UserProfileView.as_view(), name="profile"),
]
