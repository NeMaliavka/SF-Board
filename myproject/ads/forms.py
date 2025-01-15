from django import forms
from .models import Ad
from django.contrib.auth.models import User

class AdForm(forms.ModelForm):
    email = forms.EmailField(required=True)  # Обязательное поле для электронной почты

    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # Добавляем email в поля формы

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Устанавливаем пароль
        if commit:
            user.save()
        return user
