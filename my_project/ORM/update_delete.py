from models import Category, Product


# query = Product.update(price=1_000_000).where(Product.id==5)
# print(query, '!!!')
# query.execute()

# query = Product.update(title='AirPods Pro').where(Product.title=='AirPods')
# print(query, '!!!')
# query.execute()


# query = Product.update(price=(Product.price * 1.5))
# print(query, '!!!')
# query.execute()

# Удаление данных
# product = Product.get(Product.id==5)
# print(product, product.title)
# product.delete_instance()
# print(product)

query = Category.delete().where(Category.id==6)
query.execute()
