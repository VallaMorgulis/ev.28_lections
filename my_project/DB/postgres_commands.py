
# УСТАНОВКА POSTGRES
# sudo apt update
# sudo apt install postgresql postgresql-contrib
# sudo systemctl start postgresql.service
# psql --version


# команда для входа через юзера postgres:
# sudo -u postgres psql

# лщманда для выхода 
# exit

# команда для входа в своего юзера
# psql

# команда для выхода
# \q

# CREATE DATABASE valla;

# создание суперюзера
# CREATE ROLE valla SUPERUSER LOGIN PASSWORD '1';

# изменение
# ALTER USER 'username' WITH PASSWORD '1';

# даем все привелегии юзеру
# GRANT ALL PRIVILEGES ON DATABASE <databasename> TO <username>

# ПРИМЕР
# grant all privileges on database valla to valla;

# \du - все юзеры

# \l - список всех баз

# \dt - все таблицы (нужно подключиться к бд заранее)

# \c 'name' - команда для подключение к бд

# psql -U <username> -d <dbname> - подключаемся под выбранным username к dbname

# DROP DATABASE <database>; - УДАЛЕНИЕ
