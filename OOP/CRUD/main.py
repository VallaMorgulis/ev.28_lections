# from views import *
# import json

# class Product(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
#     def save(self):
#         with open('data.json', 'w') as file:
#             json.dump(self.objects, file, indent=4)
#         return 'Saved!'
    
# class Comment(CreateMixin, ReadMixin, DeleteMixin):
#     pass

# smartphones = Product()
# print(smartphones.post(title="Redmi Note 10", description='The best phone for own price', qty=10, price=250))
# print(smartphones.post(title="Redmi Note 20", description='The best flagman', qty=5, price=500))
# print(smartphones.post(title="iPhone 14 pro MAX", description='The best phone for Apple', qty=15, price=1000))
# print(smartphones.post(title="Samsung S22 Ultra", description='Flagman of Samsung', qty=7, price=650))
# print(smartphones.post(title="iPhone 13 pro MAX", description='Flagman of Apple last year', qty=5, price=750))
# print()
# print()
# print(smartphones.list())
# print()
# print(smartphones.detail(1))
# print(smartphones.patch(1, title='Redmi Note 9'))
# print()
# print(smartphones.list())
# print(smartphones.delete(-1))
# print(smartphones.delete(1))
# print(smartphones.save())




