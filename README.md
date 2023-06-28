# The Apptrix-Dating
Проект представляет собой тестовое задание для backend разработчика компании APPTRIX

Реализована следующая функциональность:
 - Регистрация нового пользователя
 - Логин с получением access и refresh токенов JWT
 - Наложение водяного полупрозрачного знака на аватар пользователя в правом нижнем углу
 - Добавление пользователя в фавориты по PATCH запросу, при взаимной симпатии происходит рассылка сообщений на почту
 - Отображение списка всех пользователей с фильтрацией по полу, имени, фамилии и расстоянию
 
---

**Технологии используемые в проекте:**
 
 - Django
 - DRF
 - Django-Filter
 - Haversine
 - Pillow
 - Gunicorn 
 - Pydantic
 - Docker
 - Docker-compose

---

**Структура проекта:**
 
 - apptrix_dating - основное приложение Django с файлом настроек
 - core - приложение для кастомной модели пользователя
 - participant - приложение для клиента (модель клиента основана на модели пользователя из core)
 - image - медиа файлы проекта, в данном случае - изображения аватаров пользователей и водяных знаков
 - docker-compose.yaml - файл с описанием всех docker контейнеров для проекта
 - manage.py - файл Django для управления проектом (запуск, миграции и т.д)
 - utils.py - вспомогательные функции для проекта 
 - README.md - файл с документацией к проекту
---

**Запуск проекта:**
Проект построен на docker контейнерах, поэтому для запуска нужно только скачать docker-compose.yaml файл и подготовить
.env файл с настройками.
Чтобы запустить проект, выполните следующие шаги:
 - Клонируйте репозиторий или можете просто скопировать docker-compose.yaml файл
 - Установите докер на ваш компьютер или VPS `sudo apt install docker.io docker-compose`
 - Подготовьте .env файл согласно представленной ниже инструкции
 - Подготовьте docker-compose.yaml файл если это нужно (вы можете указать другие порты, названия контейнеров и т.д)
 - Запустите приложение с помощью команды: `sudo docker-compose up -d --build`
 - Главная страница со swagger будет доступна по ссылке http://localhost/ (при запуске локально) или http://yourdomain/ 
(при запуске на сервере). Здесь вы можете увидеть все доступные маршруты с описанием
 - After that application is ready to process requests

---

**Примеры запросов:**

- GET: http://localhost/
- В ответ вы получите swagger с документацией

- GET: http://localhost/api/list/
- Список всех пользователей в JSON формате, доступна сортировка по query параметрам - gender(1, 2, 3),
first_name - строка по частичному совпадению в любом регистре, last_name - то же самое, distance - число с плавающей
точкой в километрах относительно текущего пользователя

- POST: http://localhost/api/clients/login/, http://localhost/api/clients/token/refresh/
- Получение или обновление access token по email и паролю зарегистрированного пользователя. Токен необходим для доступа
к другим ручкам API

- POST: http://localhost/api/clients/create/
- Регистрация нового пользователя. Лучше выполнять через form-data, чтобы иметь возможность загрузить файл аватара.
Нужно обязательно указать email, password и password_repeat и gender, остальные поля не обязательные, но лучше указать
все.

- PUT, PATCH: http://localhost/api/clients/<favorite_id>/match/
- Добавление пользователя id = favorite_id в фаворитов текущего пользователя. В фавориты можно добавить любого
существующего клиента, кроме себя самого.

---
Пример .env файла:

    POSTGRES_DB=dating  # Настройки для запуска базы данных Postgres
    POSTGRES_PASSWORD=apptrix2515
    POSTGRES_USER=apptrix
    POSTGRES_PORT=5432
    POSTGRES_HOST=localhost # Тут необходимо указать либо имя домена или имя контейнера 
                                # (при запуске приложения через докер)
    SECRET_KEY=django-insecure-5r(7#6v)daz==(04kd^)@a@34$7k054ex7y4%0)9u#6!=npchg
    DEBUG=True # Режим отладки при релизе должен быть отключен
    TITLE=The Apptrix-Dating
    DESCRIPTION=This is a test dating application for Apptrix
    VERSION=1.0.0
    EMAIL_HOST=smtp.yandex.ru  # Настройи почтового сервера их можно узнать на сайтах почтовых служб
    EMAIL_HOST_USER=youremail@yandex.ru  # например для Yandex mail - 
                                        # https://yandex.ru/support/mail/mail-clients/others.html#smtpsetting
    EMAIL_HOST_PASSWORD=your_strong_password
    EMAIL_PORT=25
    EMAIL_USE_TLS=True


The project was created by Alexey Mavrin in 28 June 2023