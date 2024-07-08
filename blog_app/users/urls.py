from django.contrib.auth import views as auth_views
from django.urls import path

import users.views as user_views

app_name = "account"

urlpatterns = [
    path("register/", user_views.register, name="register"),
    path("login/", user_views.UserLoginView.as_view(), name="login"),
    path("logout/", auth_views.logout_then_login, name="logout"),
]
