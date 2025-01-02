from django.db import models


class MailingRecipient(models.Model):
    """Получатель рассылки
    Email
    Ф. И. О.
    Комментарий """
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    comment = models.TextField()


class Message(models.Model):
    """Сообщение
    Тема письма
    Тело письма """
    subject_message = models.CharField(max_length=100)
    body_message = models.TextField()


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

    datime_first_sending = models.DateTimeField()
    datime_end_sending = models.DateTimeField()
    status_mailing = models.CharField(max_length=9, choices=STATUS_MAILOUT_CHOICES, default=CREATED,
                                      verbose_name='статус рассылки')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    recipient = models.ManyToManyField(MailingRecipient)


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

    datime_attempt = models.DateTimeField
    status_attempt = models.CharField(max_length=14, choices=STATUS_ATTEMPT_CHOICES, default=NOT_SUCCESSFULLY)
    mailing_server_response = models.TextField()
    mailout = models.ForeignKey(Mailout, on_delete=models.CASCADE)
