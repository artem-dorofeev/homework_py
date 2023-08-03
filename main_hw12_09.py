import copy
# from copy import deepcopy, copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        copy_obj = Person()
        copy_obj.name = copy(self.name)
        copy_obj.email = copy(self.email)
        copy_obj.phone = copy(self.phone)
        copy_obj.favorite = copy(self.favorite)
        return copy_obj


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

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

    def __copy__(self):
        copy_obj = Contacts()
        copy_obj.filename = copy(self.filename)
        copy_obj.contacts = copy(self.contacts)
        copy_obj.is_unpacking = copy(self.is_unpacking)
        copy_obj.count_save = copy(self.count_save)
        
        return copy_obj

        

    def __deepcopy__(self, memo):
        copy_obj = Contacts()
        memo[id(self)] = copy_obj
        copy_obj.filename = copy.deepcopy(self.filename, memo)
        copy_obj.contacts = copy.deepcopy(self.contacts, memo)
        copy_obj.is_unpacking = copy.deepcopy(self.is_unpacking, memo)
        copy_obj.count_save = copy.deepcopy(self.count_save, memo)
        
        return copy_obj
        
        
        
        


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



"""

Реалізуйте метод __copy__ для класу Person.

Реалізуйте методи __copy__ та __deepcopy__ для класу Contacts.

"""
