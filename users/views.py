from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CustomUserCreationForm


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
