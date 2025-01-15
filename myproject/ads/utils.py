import random
from .models import OneTimeCode

def send_one_time_code(user):
    code = str(random.randint(100000, 999999))  # Генерация кода
    OneTimeCode.objects.create(user=user, code=code)
