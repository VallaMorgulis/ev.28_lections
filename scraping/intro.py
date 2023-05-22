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

# ORDER BY: позволяет соритровать выводщие данные по убыванию (desc) или возрастанию (asc). ASC (по возрастанию), DESC (по убыванию).
# Синтаксис: SELECT <row> FROM <tablename> ORDER BY <row> [ASC/DESC];

# WHERE: используется для фильтрации по полям. Будут выводится только те данные, которые соответсвуют условию оператора WHERE.
# Синтаксис: SELECT <row> FROM <tablename> WHERE <row> = 'чему либо';

# BETWEEN: условие между 
# Синтаксис: SELECT <*> FROM <tablename> WHERE <row> BETWEEN <value> and <value>;

# LIKE: выводит результат ктороые соответсвует введенному шаблону для строк. Чувствителен к регистру.
# ILIKE: тоде самое, но не чувствителен к регистру.
# Синтаксис: SELECT <row> FROM <tablename> WHERE <row> LIKE/ILIKE 'чему нибудь'; ('%values%')

# AND оператор И для множественных условий.
# IN: WHERE <row> in (1,2,3,4);

# LIMIT: ставит ограничение в количестве получаемых данных

# GROUP BY: разделяет данные которые мы получаем в SELECT, при этом группируя их по определенному признаку. И теперь для каждой группы можно использовать функцию.

# HAVING: ставит условия при помощи которого данные отбираются в группировку.

# Агрегатные функции - AVG(), COUNT(), MIN(), MAX(), SUM().

# Экспорт бд(дамп):
# pg_dump -U <username> -d 'dbname' > 'file.sql'

# Импорт:
# psql -U <username> -d <dbname> -f <filename>

#------------------------------

# Связи между таблицами(relations):
#         1. Один к одному (One-to-One) - человек паспорт
#             в одну из таблиц добавляетс поле fkи дается ограничение unique
#         2. Один ко многим (One-to-Many) - человек и банковские карты
#             в таблицу добавляется много (банковские карты) допю поле fk
#         3. Много ко многим(Many-to-Many) - студенты и преподы
#             создается новая вспомогательная 3-я таблица со связями


# Ограничения:
    # 1. NOT NULL - обязетельно к заполнению
    # 2. UNIQUE - то что будут хранится только уникальные данные
    # 3. CHECK -> CHECK age > -1 - ограничение проверки на условия
    # 4. PRIMARY KEY(для установки идентификатора данных в таблице)
    # 5. FOREIGN KEY(для установки связей между таблицами)
    # 6. ON DELETE - для установки поведения при удалении данных которые были связаны

# --------------------------------------
# Change the property - изменение свойства через ADD CONSTRAIN

# ALTER TABLE <table> ADD CONSTRAINT <give the name> UNIQUE(<row>);
# ALTER TABLE imei_codes ADD CONSTRAINT id_unique UNIQUE(product_id);

# Change the row - изменение поля через ALTER COLUMN
# ALTER TABLE <table> ALTER COLUMN <name row> SET NOT NULL;
# ALTER TABLE products ALTER COLUMN title SET NOT NULL;

#---------------------------
# JOIN  - выборка данных из двух таблиц, соединение таблиц. 

# LEFT JOIN: выборка быдет содержать в себе все строки из левой таблицы

# RIGHT JOIN: выборка быдет содержать в себе все строки из правой таблицы

# SELECT bc.id, bc.bank, bc.cart_code, bc.owner, (h.name || ' ' || h.last_name) as full_name FROM bank_cards as bc
# JOIN human as h ON h.id = bc.owner;




# 1. Вытащить все произведения в котрых sourse = Moby и кол-во параграфов меньше 100
# SELECT source, totalparagraphs FROM work WHERE source = 'Moby' AND totalparagraphs < 100; 



# 2. Найти кол-во глав в каждом произведении
# select count(*), work.title from chapter join work on work.workid = chapter.workid group by work.title order by count(*) desc;

# 3. Найти сколько произведений относятся к каждому 
# select count(*), genretype from work group by genretype;

# 4. Найти кол-во параграфов в каждом произведении и вытащить названия произведений
# select count(*), work.title from paragraph join work on work.workid = paragraph.workid group by work.title;


# 5. Вытащить имена героев, чьи реплики состовляют больше 200 слов, также произведения в которых они встречаються, жанр, год выхода произдведения в порядке убывания
# select character.charname, work.title, work.genretype, work.year from character_work join character on character.charid = character_work.charid join work on work.workid = character_work.workid where character.speechcount > 200 order by work.year desc;


# 6. Вытащить героя, который чаще всех появляется в произведениях
# SELECT character.charname, COUNT(*) AS works_count FROM character_work JOIN character
# ON character.charid = character_work.charid JOIN work ON character_work.workid = work.workid
# GROUP BY character.charname ORDER BY works_count DESC LIMIT 1;


























