from register import RegisterMixin, LoginMixin

class User(RegisterMixin, LoginMixin):
    pass


obj = User()

# print(obj.register('JohnSnow3', 'John1', 'Snow2', 'bastard125', 'bastard125'))
print(obj.login('JohnSnow', 'bastard123'))


