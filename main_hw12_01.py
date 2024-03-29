import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename, "wb") as f:
        pickle.dump(contacts, f)


def read_contacts_from_file(filename):
    with open(filename, "rb") as f:
        result = pickle.load(f)
    return result


adb = {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

write_contacts_to_file("test1.bin", adb)

result = read_contacts_from_file("test1.bin")

print(result)


# import pickle


# data = {"a": [1, 2, 3, 3],
#         "b": "Hello"}

# byte_str = pickle.dumps(data)

# print(byte_str)

# unpacked_data = pickle.loads(byte_str)

# print(data == unpacked_data)

# with open("data.bin", "wb") as f:
#     pickle.dump(data, f)

# with open("data.bin", "rb") as f:
#     some_data = pickle.load(f)

# print(some_data)

"""


Є список, кожен елемент якого є словником з контактами користувача наступного виду:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

Словник містить ім'я користувача name, його email, телефонний номер phone та властивість favorite - обраний контакт чи ні.

Розробіть дві функції для серіалізації та десеріалізації списку контактів за допомогою пакета pickle та зберігання отриманих даних у бінарному файлі.

Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, contacts - список контактів. 
Вона зберігає вказаний список у файл, використовуючи метод dump пакету pickle.

Друга функція read_contacts_from_file читає та повертає зазначений список contacts з файлу filename, використовуючи метод load пакету pickle.

"""
