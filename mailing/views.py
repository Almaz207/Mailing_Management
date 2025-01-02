from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from .models import MailingRecipient, Message, Mailout, AttemptToSend


class CreateMailingRecipient(CreateView):
    pass


class CreateMessage(CreateView):
    pass


class CreateAttemptToSend(CreateView):
    pass


class CreateMailout(CreateView):
    pass
