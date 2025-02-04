from django.contrib import admin
from users.models import CustomUser

@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    list_display = ('username', 'id', 'date_joined', 'email')