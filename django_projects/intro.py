
# 1. Создать виртуальное окружение
#         python3 -m venv <venv>
# 2. Устанавливаем нужные библиотеки и джанго
#         pip install -r <library> 
# or      pip install -r <library> == <version>
#         pip freeze > requirements.txt
# 3. Создание проекта и файла manage.py
#         django-admin startproject <name> .
# 4. Создание приложения для проекта
#         python3 manage.py startapp <name>
#         django-admin startapp <name>
# 5. Записать название вашего приложения в installed apps в настройках (подключение вашего приложения в проект)
# 6. Настройка базы данных
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': '<name_of_your_db>',
#         'USER': '<sanzhar>',
#         'PASSWORD': '<1>',
#         'HOST': 'localhost',
#         'PORT': 5432
#     }
# }
# 7. Создание базы данных в постгрес
# 8. Работа с миграциями
#     8.1 Создаем файлы миграции
#         pyhton manage.py makemigrations
#     8.2 Запускаем файлы миграции
#         pyhton manage.py migrate
        

# Запуск сервера
#     pyhton manage.py runserver
# Создание суперюзера
#     pyhton manage.py createsuperuser


