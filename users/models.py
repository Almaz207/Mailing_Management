from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ful_name = models.CharField(max_length=100, verbose_name='Фамилия Имя Отчество')
    email = models.EmailField(unique=True, verbose_name='email')



