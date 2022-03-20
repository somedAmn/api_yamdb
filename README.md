# api_yamdb
api_yamdb

### Описание
Проект YaMDb собирает рейтинг и отзывы пользователей
на произведения, которые делятся на категории
(«Книги», «Фильмы», «Музыка») и жанры.

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/somedAmn/api_yamdb
```
Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов

Регистрация нового пользователя

POST:

```
http://127.0.0.1:8000/api/v1/auth/signup/
```

Получение JWT-токена

POST:

```
http://127.0.0.1:8000/api/v1/auth/token/
```

Получение пользователя по username

GET:

```
http://127.0.0.1:8000/api/v1/users/{username}/
```

Изменение данных своей учетной записи

PATCH

```
http://127.0.0.1:8000/api/v1/users/me/
```