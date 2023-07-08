class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            })
        Contacts.current_id += 1
        # Contacts.list_contacts(self)


cont = Contacts()
cont.add_contacts("Artem", "1241141", "a.e@ukr.net", True)
cont.add_contacts("Artem", "1241141", "a.e@ukr.net", True)
cont2 = Contacts()
cont2.add_contacts("Artem", "1241141", "a.e@ukr.net", True)

cont2.add_contacts('Wylie Pope', '(692) 802-2949', 'est@utquamvel.net', False)

cont2.add_contacts('Cyrus Jackson', '(501) 472-5218',
                   'nibh@semsempererat.com', False)

print(cont.list_contacts())
print(cont2.list_contacts())


"""
class Contacts:
    def __init__(self):
        self.contacts_list = []

    def add_contact(self, name, phone_number):
        contact = {
            'name': name,
            'phone_number': phone_number
        }
        self.contacts_list.append(contact)

    def get_contacts(self):
        return self.contacts_list

    def search_contact(self, name):
        for contact in self.contacts_list:
            if contact['name'] == name:
                return contact
        return None

    def remove_contact(self, name):
        for contact in self.contacts_list:
            if contact['name'] == name:
                self.contacts_list.remove(contact)
                return True
        return False


# Приклад використання класу Contacts
contacts = Contacts()

# Додати контакти
contacts.add_contact('John Doe', '1234567890')
contacts.add_contact('Jane Smith', '9876543210')
contacts.add_contact('Alice Johnson', '5555555555')

# Отримати всі контакти
all_contacts = contacts.get_contacts()
print("All contacts:")
for contact in all_contacts:
    print(contact['name'], contact['phone_number'])

# Пошук контакту за іменем
search_result = contacts.search_contact('Jane Smith')
if search_result:
    print("Search result:")
    print(search_result['name'], search_result['phone_number'])
else:
    print("Contact not found.")

# Видалення контакту за іменем
contact_removed = contacts.remove_contact('John Doe')
if contact_removed:
    print("Contact 'John Doe' removed.")
else:
    print("Contact not found.")

# Перевірка, чи контакт був видалений
all_contacts = contacts.get_contacts()
print("All contacts:")
for contact in all_contacts:
    print(contact['name'], contact['phone_number'])
    """


# print(result)
"""

Реалізуйте клас Contacts, який працюватиме з контактами. На першому етапі ми додамо два методи.

    list_contacts повертає список контактів це змінна contacts з поточного екземпляра класу
    add_contacts додає новий контакт до списку, який є змінною об'єкту - contacts

Клас Contacts містить змінну класу current_id. Ми будемо використовувати її при додаванні нового контакту 
як унікального ідентифікатора контакту. Коли ми додаємо новий контакт, то передаємо такі аргументи в 
метод add_contacts: name, phone, email та favorite. Метод повинен створити словник із зазначеними ключами та 
значеннями параметрів функції. Також необхідно додати до словника новий ключ id, значенням якого є значення змінної класу current_id.

Приклад отриманого словника:

    {
    "id": 1,
    "name": "Wylie Pope",
    "phone": "(692) 802-2949",
    "email": "est@utquamvel.net",
    "favorite": True,
}

Вказаний словник ми додаємо до списку contacts. Не забуваймо збільшувати змінну current_id на одиницю 
після кожного виклику методу add_contacts для збереження унікальності ключа id для словника.

Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді.

"""
