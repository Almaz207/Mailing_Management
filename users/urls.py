from django.contrib.auth.views import LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import CustomLoginView, CustomLogoutView, start_page, RegisterView

app_name = UsersConfig.name

urlpatterns = [
    path('', start_page, name='start_page'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(next_page='users:start_page'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
