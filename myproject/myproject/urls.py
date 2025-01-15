from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ads.urls')),  # Подключение URL приложения
    path('login/', auth_views.LoginView.as_view(), name='login'),  # URL для входа
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL для выхода
]
