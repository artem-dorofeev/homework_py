class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) == int or type(x) == float:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) == int or type(y) == float:
            self.__y = y


point = Point(-5, 100)

print(point.x)
print(point.y)
"""
class Human:
    def __init__(self, age):
        self.__age = None
        self.age = age
    
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 1 < value < 100:
            self.__age = value
        else:
            raise ValueError("Bad value")

 

У класу Point до механізму setter властивостей x і y додайте перевірку на значення, що вводиться. 
Дозвольте встановлювати значення властивостей x та y для екземпляра класу, тільки якщо вони мають числове значення (int або float).

Приклад:

point = Point("a", 10)

print(point.x)  # None
print(point.y)  # 10

           
"""
