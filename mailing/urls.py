from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import ListMailingRecipient, CreateMailingRecipient, UpdateMailingRecipient, DetailMailingRecipient, \
    DeleteMailingRecipient, ListMessage, CreateMessage, DetailMessage, UpdateMessage, DeleteMessage, ListMailout, \
    CreateMailout, DetailMailout, UpdateMailout, DeleteMailout, MailingAttempt, HomePage

app_name = MailingConfig.name

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('client_list/', ListMailingRecipient.as_view(), name='list_client'),
    path('client_create/', CreateMailingRecipient.as_view(), name='create_client'),
    path('client/<int:pk>', DetailMailingRecipient.as_view(), name='detail_client'),
    path('client/<int:pk>/update', UpdateMailingRecipient.as_view(), name='update_client'),
    path('client/<int:pk>/delete', DeleteMailingRecipient.as_view(), name='delete_client'),

    path('message', ListMessage.as_view(), name='list_message'),
    path('message_create/', CreateMessage.as_view(), name='create_message'),
    path('message/<int:pk>', DetailMessage.as_view(), name='detail_message'),
    path('message/<int:pk>/update', UpdateMessage.as_view(), name='update_message'),
    path('message/<int:pk>/delete', DeleteMessage.as_view(), name='delete_message'),

    path('mailout', ListMailout.as_view(), name='list_mailout'),
    path('mailout_create/', CreateMailout.as_view(), name='create_mailout'),
    path('mailout/<int:pk>', DetailMailout.as_view(), name='detail_mailout'),
    path('mailout/<int:pk>/update', UpdateMailout.as_view(), name='update_mailout'),
    path('mailout/<int:pk>/delete', DeleteMailout.as_view(), name='delete_mailout'),

    path('attempt_mailout/<int:pk>', MailingAttempt.as_view(), name='send_mail'),
]
