from models import Product, Category


def get_all_categories():
    return Category.select(Category.id, Category.title)

def get_all_products():
    return Product.select()

# categories = get_all_categories()
# # print(categories)
# print('Все категории в БД: ')
# for category in categories:
#     print(f'ID: {category.id} Title: {category.title}')

# print()
# products = get_all_products()
# print('Все продукты в БД')
# for product in products:
#     print(f'ID: {product.id}, Title: {product.title} -> Price: {product.price} -> Category: {product.category_id.title}')


# category_laptops = Category.get(Category.title=='laptops')
# # print(category_laptops.products, category_laptops.title)
# for product in category_laptops.products: # related_name
#     print(f'ID: {product.id}, Title: {product.title} -> Price: {product.price} -> Category: {product.category_id.title}')



