from django import forms
from .models import MailingRecipient, Message, Mailout


class RecipientForms(forms.ModelForm):
    class Meta:
        model = MailingRecipient
        fields = ['full_name', 'email', 'comment']


class MessageForms(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject_message', 'body_message']


class MailoutForms(forms.ModelForm):
    class Meta:
        model = Mailout
        fields = ['datime_first_sending', 'datime_end_sending', 'status_mailing', 'message', 'recipient']
