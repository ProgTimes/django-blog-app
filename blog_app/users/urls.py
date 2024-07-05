from django.contrib.auth import views as auth_views
from django.urls import path

from users import views

app_name = "account"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", auth_views.logout_then_login, name="logout"),
]
