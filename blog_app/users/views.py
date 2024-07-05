from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from users.forms import UserRegisterForm, UserLoginForm


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = UserLoginForm
    redirect_authenticated_user = True


def register(request):
    if request.user.is_authenticated:
        return redirect('blog:post_list')
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account successfully created. Now you can login')
            return redirect("account:login")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
