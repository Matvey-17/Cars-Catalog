# Django Car Management Application

## Описание

Это веб-приложение для управления информацией об автомобилях, созданное с использованием Django и Django REST Framework. Приложение позволяет пользователям просматривать список автомобилей, добавлять новые автомобили (только для зарегистрированных пользователей), редактировать и удалять свои записи, а также оставлять комментарии к автомобилям.

### Основные функции:
- Просмотр списка автомобилей
- Просмотр деталей автомобиля
- Добавление новых автомобилей (только для зарегистрированных пользователей)
- Редактирование и удаление собственных записей
- Оставление комментариев к автомобилям (только для зарегистрированных пользователей)
- REST API для работы с автомобилями и комментариями
- Административная панель для управления моделями автомобилей и комментариев

## Стек технологий

- Python (3.x)
- Django 
- Django REST Framework (DRF)
- SQLite (по умолчанию) или PostgreSQL (опционально)

## Установка и запуск

### Требования

- Python 3.x
- pip (пакетный менеджер Python)
- virtualenv (рекомендуется, но необязательно)

### Шаги установки

1. Клонируйте репозиторий на локальную машину:

   ```bash
   git clone https://github.com/Matvey-17/Cars-Catalog.git
   cd cars_catalog
   ```
2. Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv venv
   source venv/bin/activate  # для Linux/MacOS
   venv\Scripts\activate  # для Windows
   ```
3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```
4. Примените миграции для создания базы данных:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Создайте суперпользователя для доступа к административной панели:

   ```bash
   python manage.py createsuperuser
   ```
6. Запустите сервер разработки:

   ```bash
   python manage.py runserver 8000
   ```

## Работа с API

### Автомобили

1.	Получение списка автомобилей:
   
	•	Endpoint: GET /api/cars/

	•	Описание: Возвращает список всех автомобилей.

3.	Получение информации о конкретном автомобиле:
   
	•	Endpoint: GET /api/cars/<id>/

	•	Описание: Возвращает информацию о конкретном автомобиле.

5.	Добавление нового автомобиля:
   
	•	Endpoint: POST /api/cars/

	•	Описание: Добавление нового автомобиля (только для зарегистрированных пользователей).

7.	Обновление информации о автомобиле:
   
	•	Endpoint: PUT /api/cars/<id>/

	•	Описание: Обновление информации о существующем автомобиле (только для владельца).

9.	Удаление автомобиля:
    
	•	Endpoint: DELETE /api/cars/<id>/

	•	Описание: Удаление автомобиля (только для владельца).

### Комментарии

1.	Получение списка комментариев к автомобилю:
   
	•	Endpoint: GET /api/cars/<id>/comments/

	•	Описание: Возвращает список всех комментариев к конкретному автомобилю.

2.	Добавление комментария к автомобилю:
   
	•	Endpoint: POST /api/cars/<id>/comments/

	•	Описание: Добавление нового комментария (только для зарегистрированных пользователей).
   
