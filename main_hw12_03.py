import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["name", "email", "phone", "favorite"])
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)


def read_contacts_from_file(filename):
    result = []
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            contact_dict = {
                "name": row[0], "email": row[1], "phone": row[2], "favorite": True if row[3] == "True" else False}
            result.append(contact_dict)

    return result[1:]


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


file = "adb.csv"
# write_contacts_to_file(file, adb)
res = read_contacts_from_file(file)
print(res)
# result = read_contacts_from_file(file)
# print(result)
# print(type(result))


# import csv

# with open("data.csv") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# class Animal:
#     def __init__(self, type, age):
#         self.type = type
#         self.age = age


# animals = [Animal("Lion", 5), Animal("Wolf", 3)]

# with open("animals.csv", "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["age", "type"])
#     writer.writeheader()
#     for animal in animals:
#         writer.writerow(animal.__dict__)

"""
Є список, кожен елемент якого є словником з контактами користувача наступного виду:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

Словник містить ім'я користувача name, його email, телефонний номер phone та властивість favorite - обраний контакт чи ні.

Розробіть дві функції для серіалізації та десеріалізації списку контактів за допомогою пакету csv та зберігання отриманих даних у текстовому файлі.

Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, contacts - список контактів. 
Вона зберігає вказаний список у файлі формату csv.

Структура csv файлу має бути такою:

name,email,phone,favorite
Allen Raymond,nulla.ante@vestibul.co.uk,(992) 914-3792,False
Chaim Lewis,dui.in@egetlacus.ca,(294) 840-6685,False
Kennedy Lane,mattis.Cras@nonenimMauris.net,(542) 451-7038,True
Wylie Pope,est@utquamvel.net,(692) 802-2949,False
Cyrus Jackson,nibh@semsempererat.com,(501) 472-5218,True

Зверніть увагу, першим рядком у файлі йдуть заголовки – це назви ключів.

Друга функція read_contacts_from_file читає, виконує перетворення даних та повертає вказаний список contacts із файлу filename, збереженого раніше функцією write_contacts_to_file.

Примітка: При читанні файлу csv ми отримуємо властивість словника favorite у вигляді рядка, тобто. наприклад favorite='False' . Необхідно його привести до логічного виразу назад, щоб стало favorite=False.

"""
