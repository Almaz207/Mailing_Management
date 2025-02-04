from django.contrib import admin

from .models import MailingRecipient, Message, Mailout


@admin.register(MailingRecipient)
class AdminMailingRecipients(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'id', 'ownership')
    list_filter = ('id', 'ownership')
    search_fields = ('fullname', 'email', 'id')


@admin.register(Message)
class AdminMessages(admin.ModelAdmin):
    list_display = ('id', 'subject_message', 'body_message')
    list_filter = ('id',)
    search_fields = ('id',)


@admin.register(Mailout)
class AdminMailouts(admin.ModelAdmin):
    list_display = ('datime_first_sending', 'message', 'status_mailing', 'id', 'ownership')
    list_filter = ('id', 'ownership', 'datime_first_sending')
    search_fields = ('datime_first_sending', 'message.subject_message', 'status_mailing', 'id', 'ownership')
