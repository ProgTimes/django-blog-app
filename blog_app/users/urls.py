from django.urls import path

from users.views import UserLogin, UserRegister

app_name = "user"

urlpatterns = [
    path("login/", UserLogin.as_view(), name="login"),
    path("register/", UserRegister.as_view(), name="register"),
]
