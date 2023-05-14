import json

def search_object(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        id = args[1]
        with open('data.json', 'r') as file:
            python_obj = json.load(file)
        index = 0
        for dict_ in python_obj:
            if dict_['id'] == id:
                python_obj.pop(index)
                python_obj.insert(index, kwargs)


            

                python_obj.update(object_=dict_)
                return func(*args, **kwargs)
        python_obj.update(object_=None)
        return func(*args, **kwargs)

        # for obj in self.objects:
        #     if obj['id'] == id:
        #         kwargs.update(object_=obj)
        #         return func(*args, **kwargs)
        # kwargs.update(object_=None)
        # return func(*args, **kwargs)
    return wrapper