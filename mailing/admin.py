from django.contrib import admin

from .models import MailingRecipient


@admin.register(MailingRecipient)
class AdminMailingRecipients(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'id')
    list_filter = ('id',)
    search_fields = ('fullname', 'email', 'id')
