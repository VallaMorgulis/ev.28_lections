import json
import hashlib
import os

DIR_PATH = os.getcwd()
FILE_PATH =DIR_PATH + '/users.json'

class RegisterMixin:
    """Миксин для регистрации"""

    def _hash_password(self, password, salt=None):
        if not salt:
            salt = os.urandom(32)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('latin-1'), salt, 100_000)
        return {"password" : hashed_password , "salt" : salt}
        
    def decode_password(self,hashed_password):
        decoded_password = hashed_password.decode('latin-1').replace("'", '"')
        return decoded_password
    
    def decode_salt(self,hashed_salt):
        decoded_salt = hashed_salt.decode('latin-1').replace("'", '"')
        return decoded_salt

    def _validate_password(self, password, password2):
        if len(password) < 8:
            raise ValueError('Password is too short. Must be at least 8 symbols.')
        elif password.isdigit() or password.isalpha():
            raise ValueError('Password must contain characters and digits.')
        elif password != password2:
            raise ValueError("Passwords didn't match.")
    
    def register(self, username, first_name, last_name, password, password2):
        with open(FILE_PATH, 'r') as file:
            data = json.load(file)
            try:
                id = data[-1]['id'] + 1
            except (IndexError, ValueError):
                data = []
                id = 1
            is_username_used = any([x['username'] == username for x in data])

        self._validate_password(password,password2)

        hashed_password = self._hash_password(password)
        decoded_password = RegisterMixin.decode_password(self, hashed_password["password"])
        decoded_salt = RegisterMixin.decode_salt(self, hashed_password["salt"])
        password_dict = {"password":decoded_password,"salt":decoded_salt}

        with open(FILE_PATH, 'w') as file:
            if is_username_used:
                json.dump(data, file, indent=4)
                raise ValueError('Username is already taken.')

            user = {"id" : id, "username" : username, "first_name" : first_name, "last_name" : last_name, "password" : password_dict}
            data.append(user)
            json.dump(data, file, indent = 4)
            return {'status':201,'msg':'Successfully registered'}
        
class LoginMixin:
    """Миксин для логина"""
    def encode_salt(self,hashed_salt):
        encoded_salt = hashed_salt.replace('"',"'").encode('latin-1')
        return encoded_salt

    def login(self, username, password):
        with open(FILE_PATH,'r') as file:
            data = json.load(file)
            try:
                user = list(filter(lambda x: x['username']==username, data))[0]
            except IndexError:
                raise ValueError('Username not found.')

            encoded_salt = LoginMixin().encode_salt(user["password"]["salt"])
            encoded_password = RegisterMixin()._hash_password(password, encoded_salt)["password"]
            decoded_password = RegisterMixin().decode_password(encoded_password)
            password_dict = {"password" : decoded_password, "salt" : user["password"]["salt"]}

            if password_dict != user['password']:
                raise ValueError('Invalid password.')

        return {'status':200,'msg':'Succesfully logged in', 'user': user['username']}

obj = RegisterMixin()
print(obj.register('JohnSnow111','John','Snow','bastard822','bastard822'))

obj = LoginMixin()
print(obj.login('JohnSnow111', 'bastard822'))