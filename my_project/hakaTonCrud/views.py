import csv

class ReadCsvMixin:
    def read_csv(self):
        with open('hakaTonCrud/cars.csv', 'r') as file:
            file_reader = csv.reader(file, delimiter = ",")
            all_list = [x for x in file_reader]
        return all_list

# class WriteJsonMixin:
#     def write_json(self, obj):
#         with open('cars.csv', 'w') as file:
#             file.write(obj)

# class CreateMixin(WriteJsonMixin):
#     def _get_or_set_objects_and_id(self):
#         try:
#             self.id
#             self.objects
#         except (NameError, AttributeError):
#             self.objects = []
#             self.id = 0

#     def __init__(self) -> None:
#         self._get_or_set_objects_and_id()

#     def post(self, **kwargs): #kwargs - dict
#         self.id += 1
#         obj = dict(id=self.id, **kwargs)
#         self.objects.append(obj)
#         self.write_json(self.objects)
#         return {'status': '200 OK', 'msg': obj}

# class ListingMixin(ReadJsonMixin):
#     def list(self):
#         py_objs = self.read_json()
#         res = ''
#         for item in py_objs:
#             res += f"id: {item['id']} -> {item['mark']} {item['model']}, {item['year']}, {item['engine_cap']} л., {item['color']}, {item['body_type']}, {item['mileage']} км., цена: {item['price']}\n"    
#         return res

# class RetrieveMixin(ReadJsonMixin):

#     def detail(self, id):
#         py_objs = self.read_json()
#         for item in py_objs:
#             if item['id'] == id:
#                 return f"id: {item['id']} -> {item['mark']} {item['model']}, {item['year']}, {item['engine_cap']} л., {item['color']}, {item['body_type']}, {item['mileage']} км., цена: {item['price']}"
#         return {'status': '404 Not Found'}  

# class UpdateMixin(ReadJsonMixin, WriteJsonMixin):
    
#     def patch(self, id, **kwargs):
#         py_objs = self.read_json()
#         index = 0
#         for dict_ in py_objs:
#             if dict_['id'] == id:
#                 old_item = dict_.copy()
#                 dict_.update(kwargs)
#                 py_objs.pop(index)
#                 py_objs.insert(index, dict_)
#                 self.write_json(py_objs)           
#                 return f"Было: id: {old_item['id']} -> {old_item['mark']} {old_item['model']}, {old_item['year']}, {old_item['engine_cap']} л., {old_item['color']}, {old_item['body_type']}, {old_item['mileage']} км., цена: {old_item['price']}\nСтало: id: {dict_['id']} -> {dict_['mark']} {dict_['model']}, {dict_['year']}, {dict_['engine_cap']} л., {dict_['color']}, {dict_['body_type']}, {dict_['mileage']} км., цена: {dict_['price']}"
#             index += 1
#         return {'status': '404 Not Found'}
    
#     def add_new(self, **kwargs):
#         py_objs = self.read_json()
#         id = max([x['id'] for x in py_objs]) + 1
#         dict_ = {}
#         dict_['id'] = id
#         dict_.update(kwargs)
#         py_objs.insert(id-1, dict_)
#         self.write_json(py_objs)           
#         return f"Добавили: id: {dict_['id']} -> {dict_['mark']} {dict_['model']}, {dict_['year']}, {dict_['engine_cap']} л., {dict_['color']}, {dict_['body_type']}, {dict_['mileage']} км., цена: {dict_['price']}"

# class DeleteMixin(ReadJsonMixin, WriteJsonMixin):

#     def delete(self, id):
#         py_objs = self.read_json()
#         index = 0
#         for dict_ in py_objs:
#             if dict_['id'] == id:
#                 deleted = py_objs.pop(index)
#                 self.write_json(py_objs)               
#                 return f"Удалили: id: {deleted['id']} -> {deleted['mark']} {deleted['model']}, {deleted['year']}, {deleted['engine_cap']} л., {deleted['color']}, {deleted['body_type']}, {deleted['mileage']} км., цена: {deleted['price']}"
#             index += 1
#         return {'status': '404 Not Found'}

class FilterMixin(ReadCsvMixin):
    def filter(self):
        all_cars_list = self.read_csv()
        choice = int(input('Выберите параметр для фильтрации:\n1 - Марка\n2 - Год выпуска\n3 - Объем двигателя\n4 - Тип коробки\n5 - Цвет\n6 - Тип кузова\n7 - Тип двигателя\n8 - Пробег\n9 - Цена\nВведи соответсвующую цифру: '))
        if choice == 1:
            choice_mark = input('Введите марку: ').lower()
            proposal_cars = [x for x in all_cars_list if x[0].lower().startswith(choice_mark)]
            # print(proposal_cars)
            choice = int(input('Давайте сузим поиск! \n2 - Год выпуска\n3 - Объем двигателя\n4 - Тип коробки\n5 - Цвет\n6 - Тип кузова\n7 - Тип двигателя\n8 - Пробег\n9 - Цена\nВведи соответсвующую цифру: '))
            if choice == 2:
                choice_year = int(input('Введите год выпуска: '))
                exact_list = [x for x in proposal_cars if int(x[1].strip()) == choice_year]
                print(f'Мы нашли {len(exact_list)} машины! Сузим поиск или вывести список?')
                choice = input('Выводим список?  Y/n: ')
                if choice == 'n':
                    for x in exact_list:
                        print(f'Марка: {x[0]}, Год: {x[1]}, Объем: {x[2]}, Коробка: {x[3]}, Цвет: {x[4]}, Тип кузова: {x[5]}, Тип двигателя: {x[6]}, Руль: {x[7]}, Пробег: {x[8]} км., Цена: {x[9]} сом.')
                else:
                    choice = int(input('Давайте сузим поиск! \n3 - Объем двигателя\n4 - Тип коробки\n5 - Цвет\n6 - Тип кузова\n7 - Тип двигателя\n8 - Пробег\n9 - Цена\nВведи соответсвующую цифру: '))
                    if choice == 3:
                        choice_year = int(input('Введите диапазон желаемого объема: '))
                        exact_list = [x for x in proposal_cars if int(x[1].strip()) == choice_year]
                        print(f'Мы нашли {len(exact_list)} машины! Сузим поиск или вывести список?')
                        choice = input('Выводим список?  Y/n: ')
                        if choice == 'n':
                            for x in exact_list:
                                print(f'Марка: {x[0]}, Год: {x[1]}, Объем: {x[2]}, Коробка: {x[3]}, Цвет: {x[4]}, Тип кузова: {x[5]}, Тип двигателя: {x[6]}, Руль: {x[7]}, Пробег: {x[8]} км., Цена: {x[9]} сом.')



        #     print(proposal_word)
            # mark_filter = [x for x in py_objs if x['mark'] == choice_mark]
            # res = ''
            # for item in mark_filter:
            #     res += f"id: {item['id']} -> {item['mark']} {item['model']}, {item['year']}, {item['engine_cap']} л., {item['color']}, {item['body_type']}, {item['mileage']} км., цена: {item['price']}\n"
            # return res
        # if choice == 2:
        #     choice_year = int(input('Введите год выпуска: '))
        #     year_filter = [x for x in py_objs if x['year'] == choice_year]
        #     res = ''
        #     for item in year_filter:
        #         res += f"id: {item['id']} -> {item['mark']} {item['model']}, {item['year']}, {item['engine_cap']} л., {item['color']}, {item['body_type']}, {item['mileage']} км., цена: {item['price']}\n"
        #     return res
        # if choice == 3:
        #     choice_types = input('Выберите тип кузова:\n"седан"\n"универсал"\n"купе"\n"хэтчбек"\n"минивен"\n"внедорожник"\n"пикап"\nВаш выбор: ')
        #     body_types_filter = [x for x in py_objs if x['body_type'] == choice_types]
        #     res = ''
        #     for item in body_types_filter:
        #         res += f"id: {item['id']} -> {item['mark']} {item['model']}, {item['year']}, {item['engine_cap']} л., {item['color']}, {item['body_type']}, {item['mileage']} км., цена: {item['price']}\n"
        #     return res
        # if choice == 4:
        #     choice_color = input('Введите цвет авто: ')
        #     color_filter = [x for x in py_objs if x['color'] == choice_color]
        #     res = ''
        #     for item in color_filter:
        #         res += f"id: {item['id']} -> {item['mark']} {item['model']}, {item['year']}, {item['engine_cap']} л., {item['color']}, {item['body_type']}, {item['mileage']} км., цена: {item['price']}\n"
        #     return res
        # print(choice)

# car = FilterMixin()
# car.filter()


# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon'] 
# user = input() 
# proposal_word = [x for x in list_ if x.startswith(user)] 
# print(proposal_word)
