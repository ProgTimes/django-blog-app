import users.views as user_views
from django.contrib.auth import views as auth_views
from django.urls import path

app_name = "account"

urlpatterns = [
    path("register/", user_views.register, name="register"),
    path("login/", user_views.UserLoginView.as_view(), name="login"),
    path("edit/", user_views.UserUpdateView.as_view(), name="edit"),
    path("", user_views.UserDetailView.as_view(), name="detail"),
    path("logout/", auth_views.logout_then_login, name="logout"),
]
