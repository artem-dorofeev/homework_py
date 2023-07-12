class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if 0 < value:
            self.__x = value
        else:
            raise ValueError("Bad value")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if 0 < value:
            self.__y = value
        else:
            raise ValueError("Bad value")


point = Point(-5, 10)

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

"""
