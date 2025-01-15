from django.core.mail import send_mail
from django.conf import settings
from .models import OneTimeCode
import random

def send_one_time_code(user):
    """
    Отправляет одноразовый код на электронную почту пользователя.
    """
    code = str(random.randint(100000, 999999))  # Генерация одноразового кода
    subject = 'Ваш одноразовый код'
    message = f'Ваш одноразовый код: {code}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]

    # Отправка письма
    send_mail(subject, message, email_from, recipient_list)

    # Сохранение кода в базе данных
    one_time_code, created = OneTimeCode.objects.get_or_create(user=user)
    one_time_code.code = code
    one_time_code.save()

def notify_ad_creation(ad):
    """
    Отправляет уведомление автору объявления о создании объявления.
    """
    subject = 'Ваше объявление создано'
    message = f'Ваше объявление "{ad.title}" было успешно создано.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [ad.user.email]

    # Отправка письма
    send_mail(subject, message, email_from, recipient_list)
