import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)

        


adb = [{"name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": True, }, {"name": "Ttttt Raymond",
                              "email": "trtrtr.ante@vestibul.co.uk",
                              "phone": "(666) 914-3792",
                              "favorite": False, }, {"name": "Rrrrrr Raymond",
                                                     "email": "asasas.ante@vestibul.co.uk",
                                                     "phone": "(888) 914-3792",
                                                     "favorite": True, }]

allen = Person("Allen Raymond", "nulla.ante@vestibul.co.uk",
               "(992) 914-3792", False)
print(allen.name, allen.email)

person = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

copy_person = copy_class_person(person)

print(copy_person == person)  # False
print(copy_person.name == person.name)  # True


"""

Для копіювання екземпляра класу Person із попереднього прикладу реалізуйте функцію copy_class_person. 
Як параметр вона приймає екземпляр класу person, та повертає "поверхневу" копію об'єкта за допомогою функції copy із пакета copy.

Приклад коду:

person = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

copy_person = copy_class_person(person)

print(copy_person == person)  # False
print(copy_person.name == person.name)  # True
...

"""
