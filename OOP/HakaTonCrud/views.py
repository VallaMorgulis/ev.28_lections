from search import search_object
import json

class CreateMixin:
    def _get_or_set_objects_and_id(self):
        try:
            self.id
            self.objects
        except (NameError, AttributeError):
            self.objects = []
            self.id = 0

    def __init__(self) -> None:
        self._get_or_set_objects_and_id()

    def post(self, **kwargs): #kwargs - dict
        self.id += 1
        obj = dict(id=self.id, **kwargs)
        self.objects.append(obj)
        with open('data.json', 'w') as file:
            json.dump(self.objects, file, indent=4, ensure_ascii=False)
        return {'status': '200 OK', 'msg': obj}

class ListingMixin:
    def list(self):
        with open('data.json', 'r') as file:
            python_obj = json.load(file)
        return python_obj

class RetrieveMixin:

    def detail(self, id):
        with open('data.json', 'r') as file:
            python_obj = json.load(file)
        for dict_ in python_obj:
            if dict_['id'] == id:
                return {'status': '200 OK', 'msg': dict_}
        return {'status': '404 Not Found'}  

class UpdateMixin:
       
    def patch(self, id, **kwargs):
        with open('data.json', 'r') as file:
            python_obj = json.load(file)
        index = 0
        for dict_ in python_obj:
            if dict_['id'] == id:
                dict_.update(kwargs)
                python_obj.pop(index)
                python_obj.insert(index, dict_)
                with open('data.json', 'w') as file:
                    json.dump(python_obj, file, indent=4, ensure_ascii=False)               
                return {'status': '200 OK', 'msg': python_obj}
            index += 1
        return {'status': '404 Not Found'}  

class DeleteMixin:

    def delete(self, id):
        with open('data.json', 'r') as file:
            python_obj = json.load(file)
        index = 0
        for dict_ in python_obj:
            if dict_['id'] == id:
                python_obj.pop(index)
                with open('data.json', 'w') as file:
                    json.dump(python_obj, file, indent=4, ensure_ascii=False)               
                return {'status': '200 OK', 'msg': python_obj}
            index += 1
        return {'status': '404 Not Found'}

