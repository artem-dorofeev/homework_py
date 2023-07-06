class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


# owner1 = Owner("Artem", 40, "UA")
# owner2 = Owner("Ira", 40, "US")
# dog1 = Dog("Mila", 10, "Taksa", owner1)

# print(owner1.info())
# print(owner2.info())
# print(dog1.say(), dog1.breed, dog1.who_is_owner())
"""
Створіть два класи: CatDog та DogCat. Ці класи повинні наслідуватись від двох класів відразу: Cat та Dog. 
Після успадкування в екземпляра класу CatDog, батьківський метод say повинен повертати "Meow", а у класу DogCat — "Woof". 
Для обох зазначених класів реалізуйте метод info, який повертає рядок у наступному форматі f"{self.nickname}-{self.weight}".
"""
