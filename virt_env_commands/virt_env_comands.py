# python3 -m venv env
# source env/bin/activate


# Установка venv (Virtual Environment)
# Виртуальная среда обеспечивает изолированное пространство для проектов Python на сервере, то есть, все необходимые зависимости — исполняемые файлы, библиотеки и прочие файлы копируются в некоторый выбранный каталог, а приложение использует их, а не установленные в системе. Это позволяет обеспечить стабильность среды разработки и чистоту основной системы.

# Мы будем использовать модуль venv, часть стандартной библиотеки Python 3, который можно установить с помощью:


# sudo apt install -y python3-venv


# Создание виртуальной среды для приложения
# Создать новую среду можно с помощью модуля venv. В примере ниже мы назовем новую среду env, вы можете указать любое желаемое название.

# mkdir myapp && cd myapp
# python3 -m venv env
# Активация окружения виртуальной среды
# Активируйте виртуальную среду с помощью приведенной ниже команды, где env — это имя вашего окружения разработки.

# source env/bin/activate
# После активации строка приглашения интерпретатора команд будет иметь префикс с именем среды:

# (env) netpoint@ubuntu:~/myapp$
# Тестирование виртуальной среды
# Запустите интерпретатор Python:

# (env) netpoint@ubuntu:~/myapp$ python
# Помните, что в виртуальной среде Python 3 вместо команды python3 можно использовать python, а вместо pip3 — pip.

# Воспользуйтесь функцией print(), чтобы создать стандартную программу «Hello, World»:

# Python 3.6.5 (default, Apr  1 2018, 05:46:30
# [GCC 7.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print("Hello, World!")
# Hello, World!
# >>> quit()
# Деактивация виртуальной среды
# Для деактивации среды используйте специальную команду:

# (env) netpoint@ubuntu:~/myapp$ deactivate



