from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Ad
from .utils import send_one_time_code, notify_ad_creation
from .forms import AdForm
from django.contrib.auth.decorators import login_required


@login_required
def add_ad(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        ad = Ad(title=title, description=description, user=request.user)  # Установка текущего пользователя
        ad.save()

        # Уведомление о создании объявления
        notify_ad_creation(ad)

        return redirect('ads')
    return render(request, 'ads/add_ad.html')


@login_required
def close_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, user=request.user)  # Получаем объявление, только если оно принадлежит текущему пользователю
    ad.is_closed = True  # Устанавливаем статус закрытым
    ad.save()
    return redirect('ads')


@login_required
def edit_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)

    # Проверяем, является ли текущий пользователь автором объявления
    if request.user != ad.author:
        return redirect('ads')  # Перенаправляем, если не автор

    if request.method == 'POST':
        ad.title = request.POST['title']
        ad.description = request.POST['description']
        ad.save()
        return redirect('ad_detail', ad_id=ad.id)  # Перенаправляем на страницу объявления

    return render(request, 'ads/edit_ad.html', {'ad': ad})


def register(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_one_time_code(user)
            return redirect('ads')
    else:
        form = AdForm()
    return render(request, 'registration/register.html', {'form': form})


def ads(request):
    ads = Ad.objects.all()
    return render(request, 'ads/ad_list.html', {'ads': ads})


def home(request):
    return render(request, 'ads/home.html', {'user': request.user})


def ad_detail_view(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    return render(request, 'ads/ad_detail.html', {'ad': ad})
