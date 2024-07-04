from django.views import generic

from blog.models import Post


class UserLogin(generic.ListView):
    model = Post
    template_name = 'users/login.html'


class UserRegister(generic.ListView):
    model = Post
    template_name = 'users/register.html'
