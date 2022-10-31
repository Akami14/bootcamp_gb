"""
Создайте класс User и и его наследника класс SuperUser, которые описывают пользователя и супер-пользователя.
В классе User необходимо описать:
● Конструктор, который принимает в качестве параметров значения для атрибутов name, login и password;
● Методы для изменения и получения значений атрибутов;
● Метод show_info, который печатает в произвольном формате значения атрибутов name и login;
● Атрибут класса count для хранения количества созданных экземпляров класса User.
Необходимые условия, которые надо учесть после создания объекта:
● Атрибут name доступен и для чтения, и для изменения;
● Атрибут login доступен только для чтения;
● Атрибут password доступен только для изменения.
В классе SuperUser необходимо описать:
● Конструктор, который принимает в качестве параметров значения для атрибутов name, login, password и role;
● Метод для изменения и получения значения атрибута role;
● Метод show_info, который печатает в произвольном формате значения атрибутов name, login и role;
● Атрибут класса count для хранения количества созданных экземпляров класса SuperUser.
"""

import hashlib
import os

class User:
    count = 0

    def __init__(self, name, login, password):
        self._name = name
        self._login = login
        self._password = password
        User.count += 1


    @property
    def name(self):  #имя можно смотреть
        return self._name

    @name.setter # имя можно менять
    def name(self, value):
        self._name = value

    @property
    def login(self): # можно только смотреть сеттера не будет
        return self._login # setter не нужен так как менять не можем

    def set_password(self, value):
        if len(value) < 6:
            return False
        elif value.islower():
            return False
        elif value.isdigit():
            return False
        salt = os.urandom(32)  # Новая соль для данного пользователя
        key = hashlib.pbkdf2_hmac('sha256', value.encode('utf-8'), salt, 100000)
        self._password = key

    set_password = property(fset=set_password)


    def info(self):
        return f'login - {self._login}, Name - {self._name}, password - {self._password}'# для наглядности оставим пароль


user_1 = User('A1', 'B1', 'pasword')
print(user_1.info())
user_1.password = 'iyiuyiuy'
user_pasword_1 = '19iyiuyiuy'
user_1.set_password = user_pasword_1

if user_1._password == user_pasword_1:
    print('Пароль изменен')
else:
    print('Пароль должен содержать буквы в верхнем регистри и быть длиной 6 и более символов')


class SuperUser(User):
    scount = 0

    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)
        self._role = role
        SuperUser.scount += 1

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, user_role):
        self._role = user_role

    def info(self):
        return super().info() + f', role - {self._role} '

user_2 = SuperUser('A2', 'B2', 'weqweasqsaS1321', 'Super')
print(user_2.info())

user_pasword_2 = 'Q123499wasd'
user_2.set_password = user_pasword_2
if user_2._password == user_pasword_2:
    print('Пароль изменен')
else:
    print('Пароль должен содержать буквы в верхнем регистри и быть длино1 6 и более символов')

user_2.role = 'Admin'
user_2.name = 'Alex'
print(user_2.info())
print(f'Обычных пользователей - {User.count - SuperUser.scount}, Супер пользователей - {SuperUser.scount}')