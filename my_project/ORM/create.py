import peewee
from models import Category, Product
import random

def add_category(name):
    try:
        obj = Category(title=name.lower().strip())
        obj.save()
        print(f'Сохранили категорию {obj} {obj.title}')
    except (peewee.IntegrityError, peewee.InternalError):
        print(f'{name.lower().strip()} - эта категория уже существует')


# add_category('   Computers    ')
# add_category(' Sony Playstations    ')
# add_category('Tablets')
# add_category('earphones ')

def add_products(name, price, category_name):
    category_name = category_name.lower().strip()
    try:
        category = Category.get(title=category_name)
        # print(category, category.title, category.created_at, '!!!!!!')
    except peewee.DoesNotExist:
        print(f'Категории {category_name} не существует')
    else:
        obj = Product(title=name, price=price, category_id=category)
        obj.save()
        print(f'Сохранили товар {obj} - {obj.title}')

# add_products('Sony Playstation 5', 700, 'sony playstations')
# add_products('Aser Swift', 1000, 'laptops')
# add_products('iPhone 14 pro max', 1300, 'smartphones')
# add_products('Samsung', 1000, 'laptops')
# add_products('AirPods', 400, 'earphones')
# add_products('macbook air', 900, 'laptops')
# add_products('HP ENVY 360', 800, 'laptops')
# add_products('Dell re', 1000, 'laptops')

# -----------------------------
# добавление новых данных

# add_category('cars')

# with open('files/cars.txt', 'r') as file:
#     ls = file.readlines()
#     print(ls)
#     for x in ls:
#         name = x.strip()
#         price = random.randint(5000, 20000)
#         add_products(name, price, 'cars')

with open('files/telefon.txt', 'r') as file:
    ls = file.readlines()
    print(ls)
    for x in ls:
        name = x.strip()
        price = random.randint(200, 1300)
        add_products(name, price, 'smartphones')