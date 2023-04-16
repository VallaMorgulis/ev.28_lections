# task 1

# import json
 
# with open('task1.json') as file:
#     python_obj = json.loads(file.read())
    
# with open('task1.py', 'w') as file:
#     file.write(str(python_obj))
    

# task 2

# import json 

# with open("task2.json","r") as file: 
#     json_obj = file.read() 
#     python_obj = json.loads(json_obj)
    
# print(python_obj)

# task 3

# import json 

# python_obj = None
# json_obj = json.dumps(python_obj)
# print(json_obj)

# task 4

# import json

# json_obj = "null"
# python_obj = json.loads(json_obj)
# print(python_obj)

# task 5

# import json

# users = [
#     {
#         'name': 'John',
#         'last_name': 'Snow',
#         'age': 26,
#         'has_car': True,
#     },
#     {
#         'name': 'Sam',
#         'last_name': 'Bolt',
#         'age': 4,
#         'has_car': False,
#     }
# ]

# json_users = json.dumps(users)
# print(json_users)

# task 6

# import json

# json_products = '[{"title":"iphone","price":700,"rating":4.8},{"title":"asus","price":1300,"rating":3.9},{"title":"macbook pro","price":1500,"rating":4.9},{"title":"samsung","price":150,"rating":5.0}]'
# python_products = json.loads(json_products)
# python_products = [x['title'] for x in python_products if x['rating'] > 4]
# print(python_products)

# task 7

# import json

# with open('db.json') as file:
#     pyth_obj = json.load(file)

# for x in pyth_obj:
#     x.setdefault('description')
#     x['description'] = "..."

# with open('new_db.json', 'w') as file:
#     json.dump(pyth_obj, file)

# print(pyth_obj)

# task 8

# import json

# with open('db.json') as file:
#     pyth_dict = json.load(file)

# pyth_dict = [x for x in pyth_dict if x['id'] != 3]

# with open('new_db.json', 'w') as file:
#     json.dump(pyth_dict, file, indent=4)

# print(pyth_dict)

# task 9

# def create_new(id: int, title: str, description: str, price: int, rating:float) -> None:
#     import json

#     ls = {'id': id, 'title': title, 'description': description, 'price': price, 'rating': rating}

#     with open('db.json') as file:
#         load_ls = json.load(file)
    
#     load_ls.append(ls)

#     with open('new_db.json', 'w') as file:
#         json.dump(load_ls, file, indent=4)
    
#     # return load_ls

# print(create_new(5, 'huawey', 'cool', 200, 4.8))

# task 10

# def get_sorted(json_filename: str) -> list[dict]:
#     import json

#     with open(json_filename) as file:
#         pyth_dict = json.load(file)

#     pyth_dict = sorted(pyth_dict, key=lambda x: x['rating'], reverse=True)

#     return pyth_dict

# print(get_sorted('new_db.json'))

# task 11

# def update(id: int, title: str=None, price: int=None, rating: float=None) -> None:
#     import json

#     ls_key = ['title', 'price', 'rating']
#     ls_val = [title, price, rating]
    
#     with open('new_db.json') as file:
#         pyth_dict = json.load(file)

#     key_list = list(filter(lambda x: x if x['id'] == id else None, pyth_dict)) 

#     if not key_list:
#         raise ValueError('Нет такого ключа') 
#     else:
#         for dict_ in pyth_dict:
#             for key, val in zip(ls_key, ls_val): 
#                 if val is not None: 
#                     dict_[key] = val
        
#     with open('new_db.json', 'w') as file: 
#             json.dump(pyth_dict, file, indent=4)

# print(update(1, 'HP', 650, 5.1))

# task 12

# def search(name: str) -> list[dict]:
#     import json

#     with open('db.json') as file:
#         product_list = json.load(file)

#     proposal_list = list(filter(lambda item: item['title'].startswith(name) or item['title'].endswith(name), product_list))
#     return proposal_list
   
# print(search('sus'))

# task 13

# def filter_by_price(price: int) -> list[dict]:
#     import json

#     with open('db.json') as file:
#         product_list = json.load(file)

#     price_list = list(filter(lambda item: item['price'] >= price, product_list))
#     return price_list

# print(filter_by_price(1310))

# task 14

# import json

# dict_ = [
#     {'id': 5,"title":"hp","price":750,"rating":4.7},
#     {'id': 6,"title":"huawey","price":800,"rating":4.9},
#     {'id': 7,"title":"dell","price":1600,"rating":4.8},
#     {'id': 8,"title":"aser","price":850,"rating":3.0}
# ]

# def bulk_create(products: list[dict]) -> None:
#     import json

#     with open('db.json') as file:
#         product_list = json.load(file)

#     id_ = [i['id'] for i in product_list]

#     for item in products:
#         if not item['id'] in id_:
#             product_list.append(item)

#     with open('new_db.json', 'w') as file:
#         json.dump(product_list, file, indent=4)

# bulk_create(dict_)
    



