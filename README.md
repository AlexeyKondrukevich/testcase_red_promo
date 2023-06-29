# testcase_red_promo
Оффлайн-библиотека

## Запуск проекта через Docker

- Клонировать репозиторий
- Создать файл .env со следующим содержанием:

```
SECRET_KEY=django-insecure-tv5%i7c^a7-n(o5bi_7w5y3$*wwho8g8q7a4^osruq!rg9l5(0
DEBUG=True
ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0

POSTGRES_USER=library
POSTGRES_PASSWORD=library

DB_HOST=db
DB_PORT=5432
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_NAME=library
```

- В директории testcase_red_promo выполнить

```
sudo docker-compose up -d
```

Документацию к API с примерами запросов можно посмотреть [тут](http://127.0.0.1:8000/swagger/) (при развернутом проекте)
