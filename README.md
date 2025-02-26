# Django Ads Project

## Описание проекта

Этот проект представляет собой веб-приложение для размещения и управления объявлениями. Пользователи могут регистрироваться, входить в систему, добавлять объявления, редактировать их, закрывать и просматривать список объявлений. Проект использует Django как фреймворк для разработки и SQLite в качестве базы данных.

## Функциональные возможности

- Регистрация и аутентификация пользователей
- Добавление, редактирование и закрытие объявлений
- Просмотр списка объявлений
- Отображение статуса объявления (открыто/закрыто)
- Имя автора объявления отображается рядом с ним

## Установка

### Предварительные требования

- Python 3.x
- Django 5.x
- SQLite (входит в стандартную библиотеку Python)

### Шаги по установке

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш_пользователь/ваш_репозиторий.git
   cd ваш_репозиторий
Установите необходимые зависимости:
pip install -r requirements.txt


Выполните миграции базы данных:
python manage.py migrate

Запустите сервер разработки:
python manage.py runserver

Откройте браузер и перейдите по адресу http://127.0.0.1:8000/.

### Использование
Перейдите на главную страницу, чтобы просмотреть список объявлений.

Зарегистрируйтесь или войдите в систему, чтобы добавить новое объявление.

После добавления объявления Вы сможете редактировать или закрывать его.

Статус объявления будет отображаться в списке (открыто/закрыто).

### Структура проекта:
myproject/

│

├── ads/                  # Приложение для управления объявлениями

│   ├── migrations/       # Миграции базы данных

│   ├── templates/        # Шаблоны HTML

│   ├── __init__.py

│   ├── admin.py

│   ├── apps.py

│   ├── forms.py          # Формы для работы с объявлениями

│   ├── models.py         # Модели базы данных

│   ├── tests.py

│   └── views.py          # Представления для обработки запросов

│

├── myproject/            # Основной проект

│   ├── __init__.py

│   ├── settings.py       # Настройки проекта

│   ├── urls.py           # URL маршруты

│   └── wsgi.py

│

├── manage.py             # Скрипт для управления проектом

└── requirements.txt      # Зависимости проекта
