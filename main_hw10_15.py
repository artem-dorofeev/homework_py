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
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for i in self.contacts:
            if i["id"] == id:
                return i
        return None


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

Продовжуємо розширювати функціональність класу Contacts. На цьому етапі ми додамо до класу метод get_contact_by_id. 
Метод повинен шукати контакт по унікальному id у списку contacts та повертати словник з нього із зазначеним ключем id. 
Якщо словника із зазначеним id у списку contacts не знайдено, метод повертає None.

Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді.


"""
