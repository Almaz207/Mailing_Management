from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='email')
    phone_number = models.CharField(max_length=25, null=True, blank=True, verbose_name='номер телефона')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = [
            ('mailing_permission', 'mailing pemission'), #блокировка(просмотра редакции) рассылок
            ('disabling_users', 'disabling users'), #блокировка пользователей
            ('disabling_mailing', 'disabling mailing'), #блокировка рассылок
        ]

    def __str__(self):
        return self.email
