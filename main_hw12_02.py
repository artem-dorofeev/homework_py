import json


def write_contacts_to_file(filename, contacts):
    with open(filename, "w") as f:
        json.dump({"contacts": contacts}, f)


def read_contacts_from_file(filename):
    with open(filename, "r") as f:
        result = json.load(f)
    return result['contacts']


adb = {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

# data = json.dumps(adb.__dict__)

# read_data = json.loads(data)
file = "data.json"
write_contacts_to_file(file, adb)
result = read_contacts_from_file(file)
print(result)
print(type(result))


# import json


# class Hotel:
#     def __init__(self, name, rooms):
#         self.name = name
#         self.rooms = rooms

#     @staticmethod
#     def from_json(json_str):
#         print(json_str)
#         return Hotel(**json_str)

# hotel = Hotel("Continental", 220)

# data = json.dumps(hotel.__dict__)

# hotel1 = json.loads(data, object_hook=Hotel.from_json)

# # hotel1 = Hotel(**hotel_json)

# print(hotel1.name, hotel1.rooms)

"""

Є список, кожен елемент якого є словником з контактами користувача наступного виду:

{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

Словник містить ім'я користувача name, його email, телефонний номер phone та властивість favorite - обраний контакт чи ні.

Розробіть дві функції для серіалізації та десеріалізації списку контактів за допомогою пакету json та зберігання отриманих даних у текстовому файлі.

Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, contacts - список контактів. 
Вона зберігає вказаний список у файл, використовуючи метод dump пакету json.

Структура json файлу має бути такою:

{
  "contacts": [
    {
      "name": "Allen Raymond",
      "email": "nulla.ante@vestibul.co.uk",
      "phone": "(992) 914-3792",
      "favorite": false
    },
    ...
  ]
}

Тобто список контактів повинен зберігатися за ключем "contacts", а не просто зберегти список у файл.

Друга функція read_contacts_from_file читає та повертає зазначений список contacts з файлу filename, збереженого раніше функцією write_contacts_to_file, використовуючи метод load пакету json.


"""
