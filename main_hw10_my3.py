from collections import UserDict
from normalize_phone import normalize_phone


class Field:
    def __init__(self, value) -> None:
        self.value = value


class Name(Field):
    def __init__(self, name) -> None:
        self.name = name
    # pass


class Phone(Field):
    def __init__(self, phone, name: Name = None) -> None:
        self.phone = normalize_phone(phone)
        self.name = name

    # def set_number(self):
    #     return normalize_phone(self.number)


class Record():
    def __init__(self, name: Name, phone: Phone = None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)


class AddressBook(UserDict):
    def add_record(self, rec: Record):
        self.data[rec.name.value] = rec
        print(self)


def main():
    artem = Name('artem')
    # print(artem.value)
    ph = Phone('=38050(484)6925')
    print(ph.phone)
    user1 = AddressBook
    print(user1.add_record(artem, ph))


if __name__ == "__main__":
    main()
