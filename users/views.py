from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import CustomUserCreationForm, CustomUserUpdateForm
from users.models import CustomUser


def start_page(request):
    return render(request, template_name='users/start_page.html')


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'users/logout.html'


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'users/users_list.html'
    context_object_name = 'users_objects'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:list_users')
