from django.db import models
from users.models import CustomUser


class MailingRecipient(models.Model):
    """Получатель рассылки
    Email
    Ф. И. О.
    Комментарий """
    email = models.EmailField(unique=True, verbose_name='email')
    full_name = models.CharField(max_length=100, verbose_name='Имя клиента')
    comment = models.TextField(verbose_name='Комментарий')
    ownership = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, verbose_name='Владелец', null=True, blank=True)

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'


class Message(models.Model):
    """Сообщение
    Тема письма
    Тело письма """
    subject_message = models.CharField(max_length=100, verbose_name='Тема письма')
    body_message = models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        return f'{self.subject_message}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Mailout(models.Model):
    """Рассылка
    Дата и время первой отправки (datetime).
    Дата и время окончания отправки (datetime).
    Статус (строка:'Завершена','Создана','Запущена').
    Сообщение (внешний ключ на модель «Сообщение»).
    Получатели («многие ко многим», связь с моделью «Получатель»)"""

    CREATED = 'created'
    COMPLETED = 'completed'
    LAUNCH = 'launch'

    STATUS_MAILOUT_CHOICES = [
        (CREATED, 'создана'),
        (LAUNCH, 'запущена'),
        (COMPLETED, 'завершена'),
    ]

    datime_first_sending = models.DateTimeField(verbose_name='дата и время первой отправки')
    datime_end_sending = models.DateTimeField(verbose_name='дата и время последней отправки', null=True, blank=True)
    status_mailing = models.CharField(max_length=9, choices=STATUS_MAILOUT_CHOICES, default=CREATED,
                                      verbose_name='статус рассылки')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    recipient = models.ManyToManyField(MailingRecipient, verbose_name='Получатели')
    ownership = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, verbose_name='Владелец', null=True, blank=True)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        return f'{self.message}'


class AttemptToSend(models.Model):
    """Попытка рассылки
    Дата и время попытки (datetime).
    Статус ('Успешно','Не успешно').
    Ответ почтового сервера (текст).
    Рассылка """

    SUCCESSFULLY = 'successfully'
    NOT_SUCCESSFULLY = 'not successful'

    STATUS_ATTEMPT_CHOICES = [
        (SUCCESSFULLY, 'успешно'),
        (NOT_SUCCESSFULLY, 'не успешно'),
    ]

    datime_attempt = models.DateTimeField(auto_now_add=True)
    status_attempt = models.CharField(max_length=14, choices=STATUS_ATTEMPT_CHOICES, default=NOT_SUCCESSFULLY,
                                      verbose_name='статус рассылки')
    mailing_server_response = models.TextField(verbose_name='ответ почтового сервера')
    mailout = models.ForeignKey(Mailout, on_delete=models.CASCADE, verbose_name='рассылка')


    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
