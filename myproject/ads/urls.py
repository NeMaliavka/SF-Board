from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, ads, home, add_ad, ad_detail_view, close_ad, edit_ad

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('ads/', ads, name='ads'),
    path('add/', add_ad, name='add_ad'),
    path('ad/<int:ad_id>/', ad_detail_view, name='ad_detail'),
    path('close/<int:ad_id>/', close_ad, name='close_ad'),  # Новый маршрут для закрытия объявления
    path('edit/<int:ad_id>/', edit_ad, name='edit_ad'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Путь для выхода
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Путь для входа
]

