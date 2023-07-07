from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        key_list = []
        for key, val in self.items():
            if val == value:
                key_list.append(key)
        return key_list


test_dict = LookUpKeyDict({"a": 1,
                           "b": 2,
                           "c": 1})

print(test_dict.lookup_key(1))


# cat = CatDog("koshka", 5)
# dog = DogCat("pesel", 8)

# print(cat.info(), dog.info())
"""

У четвертому модулі ми реалізували функцію lookup_key для пошуку всіх ключів за значенням у словнику. 
Першим параметром у функцію ми передавали словник, а другим – значення, яке хотіли знайти. 
Результатом був список ключів або порожній список, якщо ми нічого не знаходили.

def lookup_key(data, value):
    keys = []
    for key in data:
        if data[key] == value:
            keys.append(key)
    return keys

Створіть клас LookUpKeyDict, батьком якого буде клас UserDict. Зробіть функцію lookup_key методом класу LookUpKeyDict.

"""
