from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from users.forms import UserLoginForm, UserRegisterForm, UserUpdateForm
from users.models import User


class UserLoginView(LoginView):
    template_name = "users/login.html"
    authentication_form = UserLoginForm
    redirect_authenticated_user = True


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "users/detail.html"
    context_object_name = "user"

    def get_object(self):
        return self.request.user


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "users/edit.html"
    context_object_name = "user"

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy("account:detail")

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect(self.get_success_url())
        return self.form_invalid(form)


def register(request):
    if request.user.is_authenticated:
        return redirect("blog:post_list")
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Account successfully created. Now you can login")
            return redirect("account:login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})
