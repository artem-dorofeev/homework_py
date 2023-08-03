import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0
        self.is_unpacking = False
        

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

        


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

persons = Contacts("user_class.dat", adb)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons.is_unpacking)  # False
print(person_from_file.is_unpacking)  # True


"""


Продовжуємо розширювати приклад із попереднього завдання. Додайте до класу Contacts атрибут is_unpacking, 
за замовчуванням він повинен мати значення False. Реалізуйте магічний метод __setstate__ для класу Contacts. 
При розпаковуванні екземпляра класу метод повинен змінювати значення атрибута is_unpacking на значення True. 
Таким чином, ця властивість визначатиме, що екземпляр класу отримано внаслідок розпакування.

Приклад роботи коду:

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons.is_unpacking)  # False
print(person_from_file.is_unpacking)  # True



"""
