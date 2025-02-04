from config.settings import CACHE_ENABLED
from django.core.cache import cache
from mailing.models import MailingRecipient, Message, Mailout


class MailingService:

    @staticmethod
    def get_all_recipient():
        if CACHE_ENABLED:
            key = 'recipients'
            recipients = cache.get(key)
            if recipients is None:
                recipients = MailingRecipient.objects.all()
                cache.set(key, recipients, 120)
        else:
            recipients = MailingRecipient.objects.get.all()
        return recipients

    @staticmethod
    def get_all_mailout():
        if CACHE_ENABLED:
            key = 'mailout'
            mailout = cache.get(key)
            if mailout is None:
                mailout = Mailout.objects.all()
                cache.set(key, mailout, 120)
        else:
            mailout = Mailout.objects.get.all()
        return mailout

    @staticmethod
    def get_all_massage():
        if CACHE_ENABLED:
            key = 'messages'
            messages = cache.get(key)
            if messages is None:
                messages = Message.objects.all()
                cache.set(key, messages, 120)
        else:
            messages = Message.objects.get.all()
        return messages
