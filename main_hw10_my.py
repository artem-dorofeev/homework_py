from collections import UserDict, UserList
from normalize_phone import normalize_phone


class AddressBook(UserDict):
    # def __init__(self):
    #     self.addressbook = {}

    def add_record(self, rec):
        self["name"] = str(rec)
        print(self.data)

    def add(*args):
        name = Name(args[0])
        phone = Phone(args[1])
        rec = Record(name, phone)
        return f'ok'
        # return addressbook.add_rec(rec)

    def add_phone(phone):
        pass


class Field():
    pass


class Name:
    def __init__(self, name) -> None:
        self.name = name


class Phone():
    def __init__(self, number) -> None:
        self.number = number


class Record():
    def __init__(self, name) -> None:
        self.name = name.name

    

    """Клас Record, який відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name."""
    pass


if __name__ == "__main__":

    ab = AddressBook()
    name = Name("Bill")
    print(name.name)
    phone1 = Phone("12345")
    print(phone1.number)
    rec = Record(name)
    print(rec.name)

    # ab.add_record(rec)
    ab.add(rec)

    # ab.add_record(Record(Name("Jill")))

    # for rec in ab.values():
    #     assert isinstance(rec, Record)

    # phone2 = Phone("56784")
    # print(ab)

    # rec = ab["Jill"]
    # print(rec)

    # rec.add_phone(phone2)
    # print(rec)

    # rec.change_phone(Phone("56784"), Phone("99345"))

    # print(ab)
