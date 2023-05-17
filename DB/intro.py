# POSTGRESQL - система управления базами данных. (СУБД/DBMS)
# Это ряд программ и инстррументов позволяющих создавть БД, управлять ею и манипулировать данными внутри(CRUD)

# Postrgres - это сама база данных, она объектно-реляционная, т.е. данные хранятся в виде таблиц и таблицы имеют связи между собой.

# SQL (Structured Query Language) - декларативный язык структурированных запросов, он применется для создания и получения данных при помощи запросов в БД.

#---------------------------------------

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


# \du - все юзеры

# \l - список всех баз

# \dt - все таблицы (нужно подключиться к бд заранее)

# \d 'name' - подробная информация про таблицу

# \c 'name' - команда для подключение к бд

# psql -U <username> -d <dbname> - подключаемся под выбранным username к dbname

# DROP DATABASE <database>; - УДАЛЕНИЕ

# -------------------------------------------

# Типы полей в Postrges

# Numeric Types(числовые типы)
#     a. smallint(2 bytes) -> -32767 to 32767
#     b. integer(4 bytes) -> -2_147... to 2_147...    millions
#     c. bigint(8 bytes) -> ....
#     d. real(4 bytes) -> число с плавающей точкой, вещественное число (6 цифр после запятой)
#     f. double precsion (8 bytes) -> real, но только с двойной точностью (6 цифр после запятой)
#     g. serial(4 bytes) -> integer, auto-increment

# Character types(Символьный типы(строковые))
    # a. varchar(количество символов) -> если укажем 50, а заполним только 10, то остальные будут свободны. Максимально колтчество символов 255
    # b. char(количество символов) -> если укажем 50, а заполним только 10, то остальные будут заполнены пробелами. Максимально колтчество символов 255
    # c. text() -> неограниченное количество символов.

# Boolen Type
    # a. boolean(1 byte) -> True/False

# Date -> календарная дата (год, месяц, день)

# location -> координатная точка (x, y) - (245, -12)

# # Enumerate types:
#     ('a', 'b', 'c')
# CREATE TYPE <any name> AS ENUM ('Happy', 'Sad', 'Mad')


#-------------------------
#  Команда для создания таблицы

# CREATE TABLE <table name> (
#     <colum> <type>
# )

# ПРИМЕР
# CREATE TABLE films (
    # code char(5), 
    # title varchar(100),
    # date date,
    # genre varchar(50),
    # budget integer,
    # country varchar(50),
    # id serial
    # );

# DROP TABLE <name> - удаление таблицы

# Команда для добавления данных в таблицу
# INSERT INTO <tablename> [(colums)] VALUES (data), (data);

# ПРИМЕР 
# INSERT INTO films (code, title, date, genre, budget, country) VALUES
# ('AU56', 'Game of Thrones', '2015-03-31', 'Fantasy', 1000000, 'USA'),
# ('het5', 'Lord of the Rings', '2001-06-12', 'Fantasy', 12000000, 'USA');

# Команда для получения данных
# SELECT (colums) * FROM <table> - звездочка указывает на все товары.

# Команда для обновления данных
# UPDATE <table> SET <column> = <new_value> WHERE <column> = <value>;

# Команда для удаления данных
# DELETE FROM <table> WHERE <column> = <value>;

















