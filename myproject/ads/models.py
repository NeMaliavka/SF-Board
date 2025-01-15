from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ads')
    is_closed = models.BooleanField(default=False)  # Поле для отслеживания статуса объявления
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads', null=True, blank=True)

    def __str__(self):
        return self.title

class OneTimeCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
