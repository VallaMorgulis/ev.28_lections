from views import *

class Cars(CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DeleteMixin, FilterMixin): 
    ...


car = Cars()
print(car.post(mark='BMW', model='5 серия', year=2017, engine_cap=2.0, color='черный', body_type='седан', mileage=50000, price=4015800.00))
print(car.post(mark='Mersedes', model='GLA', year=2019, engine_cap=2.6, color='белый', body_type='седан', mileage=25000, price=5014500.00))
print(car.post(mark='Корыто', model='Волшебной серия', year=253, engine_cap=0.1, color='пегий', body_type='универсал', mileage=50000000, price=4.00))
print(car.post(mark='Subaru', model='forester', year=2021, engine_cap=2.5, color='синий', body_type='внедорожник', mileage=10000, price=3015800.00))
print(car.post(mark='Toyota', model='Camry', year=2018, engine_cap=2.0, color='белый', body_type='седан', mileage=56000, price=2015800.00))
# print(car.list())
# print(car.detail(3))  
# print(car.patch(3, mark='Volkswagen', model='golf', year=2015, engine_cap=1.6, color='серый', body_type='уничерсал', mileage=100000, price=1500600.00))
# print(car.delete(3))
# print(car.add_new(mark='Volkswagen', model='golf', year=2015, engine_cap=1.6, color='серый', body_type='уничерсал', mileage=100000, price=1500600.00))
# print(car.filter())






