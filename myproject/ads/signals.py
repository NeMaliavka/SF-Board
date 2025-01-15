from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OneTimeCode
from django.core.mail import send_mail

@receiver(post_save, sender=OneTimeCode)
def send_code(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Ваш одноразовый код',
            f'Ваш код: {instance.code}',
            'from@example.com',
            [instance.user.email],
            fail_silently=False,
        )
