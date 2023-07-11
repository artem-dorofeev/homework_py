from collections import UserDict
    
    
class Field:
    def __init__(self, value) -> None:
        self.value = value
        
        
class Name(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
        
    
    
class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
    
    
class Record():
    def __init__(self, name:Name, phone:Phone=None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)


class AddressBook(UserDict):
    # def __init__(self):
    #     self.addressbook = {}
    def add_record(self, rec:Record):
        self.data[rec.name.value] = rec
        print(self)
        print(self.data)
    # def add_phone(phone):
    #     pass

def main():
    user1 = Name('Artem')
    print(user1.value)
    user1_phone = Phone('+38000')
    print(user1_phone.value)
    rec_ph = Record(user1, user1_phone)
    # print(rec_ph.name, rec_ph.phones)
    adr_b = AddressBook()
    print(adr_b.add_record(rec_ph))

if __name__ == "__main__":
    main()
    print('ok')