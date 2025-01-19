from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView, View, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipientForms, MessageForms, MailoutForms
from .models import MailingRecipient, Message, Mailout, AttemptToSend
from .service import MailingService


class CreateMailingRecipient(LoginRequiredMixin, CreateView):
    model = MailingRecipient
    form_class = RecipientForms
    template_name = 'mailing/recipient_form.html'
    success_url = reverse_lazy('mailing:list_client')

    def form_valid(self, form):
        recipient = form.save()
        user = self.request.user
        recipient.ownership = user
        recipient.save()
        return super().form_valid(form)


class ListMailingRecipient(LoginRequiredMixin, ListView):
    model = MailingRecipient
    template_name = 'mailing/recipient_list.html'
    context_object_name = 'recipients'

    def get_queryset(self):
        queryset = MailingService.get_all_recipient()
        user = self.request.user
        if user.has_perm('users.mailing_permission'):
            return queryset
        else:
            return queryset.filter(ownership=user)


class DetailMailingRecipient(LoginRequiredMixin, DetailView):
    model = MailingRecipient
    form_class = RecipientForms
    template_name = 'mailing/recipient_detail.html'


class UpdateMailingRecipient(LoginRequiredMixin, UpdateView):
    model = MailingRecipient
    form_class = RecipientForms
    template_name = 'mailing/recipient_form.html'
    success_url = reverse_lazy('mailing:list_client')


class DeleteMailingRecipient(LoginRequiredMixin, DeleteView):
    model = MailingRecipient
    template_name = 'mailing/recipient_delete.html'
    success_url = reverse_lazy('mailing:list_client')


class CreateMessage(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForms
    template_name = 'mailing/message_form.html'
    success_url = reverse_lazy('mailing:list_message')


class ListMessage(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'mailing/message_list.html'
    context_object_name = 'messages'

    def get_queryset(self):
        queryset = MailingService.get_all_massage()
        return queryset


class DetailMessage(LoginRequiredMixin, DetailView):
    model = Message
    form_class = MessageForms
    template_name = 'mailing/message_detail.html'


class UpdateMessage(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForms
    template_name = 'mailing/message_form.html'
    success_url = reverse_lazy('mailing:list_message')


class DeleteMessage(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'mailing/message_delete.html'
    success_url = reverse_lazy('mailing:list_message')


class CreateMailout(LoginRequiredMixin, CreateView):
    model = Mailout
    form_class = MailoutForms
    template_name = 'mailing/mailout_form.html'
    success_url = reverse_lazy('mailing:list_mailout')

    def form_valid(self, form):
        mailout = form.save()
        user = self.request.user
        mailout.ownership = user
        mailout.save()
        return super().form_valid(form)


class ListMailout(LoginRequiredMixin, ListView):
    model = Mailout
    template_name = 'mailing/list_mailout.html'
    context_object_name = 'mailings'

    def get_queryset(self):
        queryset = MailingService.get_all_mailout()
        user = self.request.user
        if user.has_perm('users.mailing_permission'):
            return queryset
        else:
            return queryset.filter(ownership=user)


class DetailMailout(LoginRequiredMixin, DetailView):
    model = Mailout
    form_class = MailoutForms
    template_name = 'mailing/mailout_detail.html'


class UpdateMailout(LoginRequiredMixin, UpdateView):
    model = Mailout
    form_class = MailoutForms
    template_name = 'mailing/mailout_form.html'
    success_url = reverse_lazy('mailing:list_mailout')


class DeleteMailout(LoginRequiredMixin, DeleteView):
    model = Mailout
    template_name = 'mailing/mailout_delete.html'
    success_url = reverse_lazy('mailing:list_mailout')


class MailingAttempt(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        # template_name = 'mailing/attempt_mailing.html'
        mailout = get_object_or_404(Mailout, pk=pk)
        return render(request, 'mailing/attempt_mailing.html', {"mailout": mailout})

    def post(self, request, pk, *args, **kwargs):
        mailout = get_object_or_404(Mailout, pk=pk)
        if mailout.status_mailing:
            print(mailout.status_mailing)
            recipients = mailout.recipient.all()
            mailout.status_mailing = 'запущена'
            for recipient in recipients:
                try:
                    send_mail(
                        subject=mailout.message.subject_message,
                        message=mailout.message.body_message,
                        from_email="django.formeiling@yandex.ru",
                        recipient_list=[recipient.email]
                    )

                    AttemptToSend.objects.create(
                        status_attempt='успешно',
                        mailing_server_response='Сообщение успешно отправлено',
                        mailout=mailout
                    )

                except Exception as exception:
                    AttemptToSend.objects.create(
                        status_attempt='не успешно',
                        mailing_server_response=str(exception),
                        mailout=mailout
                    )

        mailout.status_mailing = 'завершена'
        mailout.save()
        return redirect('mailing:list_mailout')


class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'mailing/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['quantity_mailing'] = len(Mailout.objects.all())
        context['launch_mailing'] = Mailout.objects.filter(status_mailing='запущена').count()
        context['quantity_recipient'] = MailingRecipient.objects.distinct().count()
        return context
