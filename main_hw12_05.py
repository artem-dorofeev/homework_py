import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None, count_save=0):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = count_save

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes['count_save'] += 1
        return attributes


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

"""


Ми продовжимо розширювати приклад попереднього завдання. Додайте до класу Contacts атрибут count_save, 
за замовчуванням він повинен мати значення 0. Реалізуйте магічний метод __getstate__ для класу Contacts. 
При упаковуванні екземпляра метод класу повинен збільшувати значення атрибута count_save на одиницю. 
Таким чином, ця властивість - лічильник повторних операцій пакування екземпляра класу

Приклад роботи коду:

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
first = persons.read_from_file()
first.save_to_file()
second = first.read_from_file()
second.save_to_file()
third = second.read_from_file()

print(persons.count_save)  # 0
print(first.count_save)  # 1
print(second.count_save)  # 2
print(third.count_save)  # 3


"""
