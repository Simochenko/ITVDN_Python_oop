# class Point:
#     WIDTH = 5
#     __slots__ = ["__x", "__y"]
#
#     def __init__(self, x = 0, y = 0):
#         self.__x = x; self.__y = y
#
#     def __checkValue(x):
#         if isinstance(x, int) or isinstance(x, float):
#             return True
#         return False
#
#     def setCorrds(self, x, y):
#         if Point.__checkValue(x) and Point.__checkValue(y):
#             self.__x = x
#             self.__y = y
#
#         else:
#             print("Координаты должны быть числами")
#
#     def getCoords(self):
#         return self.__x, self.__y
#
#     # def __getattribute__(self, item):
#     #     if item == "_Point__x":
#     #         return "Частная строка"
#     #     else:
#     #         return object.__getattribute__(self, item)
#     #
#     # def __setattr__(self, key, value):
#     #     if key == "WIDTH":
#     #         raise AttributeError
#     #     else:
#     #         self.__dict__[key] = value
#     #
#     # def __getattr__(self, item):
#     #     print("__getattr__:" + item)
#     #
#     # def __delattr__(self, item):
#     #     print("__delattr__:" + item)
#
#
# pt = Point(1, 2)
# print(pt.getCoords())
# print(pt._Point__x)
# # pt.WIDTH = 5
# pt.zzz
# pt.z = 1
# del pt.z


# Property. Геттеры, сеттеры и т.д.

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


a = BankAccount('Ivan', 100)
# Можем обратиться к любому атрибуту, потому что они публичные
print(a.name)
print(a.balance)            # что не есть хорошо
a.balance = 'hello'         # прямо очень нехорошо
print(a.balance)
print()


# Сделаем атрибут balance приватным (__) и создадим интерфейс для работы с ним снаружи класса
class BankAccount2:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # геттер
    def get_balance(self):
        return self.__balance

    # сеттер
    def set_balance(self, value):
        # проверяем введённое значение баланса на корректность
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value


b = BankAccount2('Vasya', 100)
try:
    print(b.balance)            # Выдаст ошибку AttributeError, потому что атрибут баланс приватный
except AttributeError:
    print('balance - приватный атрибут, нельзя обращаться к нему напрямую')
print()
print(b.get_balance())          # Но теперь мы можем обращаться к атрибуту balance через методы
b.set_balance(400)              # Но теперь мы можем обращаться к атрибуту balance через методы
print(b.get_balance())
print(b.__dict__)               # Заглянем в атрибуты экземпляра b
print()

try:
    b.set_balance('hello')      # Пробуем подсунуть в атрибут balance какую-нибудь гадость, получим ValueError
except ValueError:
    print('Баланс должен быть числом')
print(b.get_balance())          # Значение атрибута при этом не изменится
print()

# Вызов методов, реализующих доступ к атрибуту balance неинтуитивен и неудобен.
# Хотелось бы получать доступ к атрибуту через стандартные конструкции типа b.balance
# Добавим в класс свойство.


class BankAccount3:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # геттер
    def get_balance(self):
        print('get balance')
        return self.__balance

    # сеттер
    def set_balance(self, value):
        print('set balance')
        print(value)
        # проверяем введённое значение баланса на корректность
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    # делитер
    def delete_balance(self):
        print('delete balance')
        del self.__balance

    # зададим свойство
    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)


d = BankAccount3('Misha', 400)
# Теперь мы можем обращаться к приватному атрибуту через стандартные конструкции, скрыто вызывая геттер, сеттер или
# делитер
# заданные в свойствах balance при помощи аргументов fget=, fset= и fdel=
print(d.balance)
print()
d.balance = 777
print(d.balance)
print()
d.delete_balance()
try:
    print(d.balance)
except AttributeError:
    print('Такого атрибута не существует')
print()
d.balance = 999
print(d.balance)
