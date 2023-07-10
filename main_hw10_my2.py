from collections import UserDict

class AddressBook(UserDict):
    def add(*args):
        name = Name(args[0])
        phone = Phone(args[1])
        rec = Record(name, phone)
        return addressbook.add_rec(rec)

#     def add_record(self, cont):
#         self.data["name"] = cont
#         return self.data

# class Test(UserDict):
#     def add(*args):
#         name = Name(args[0])
#         phone = Phone(args[1])
#         rec = Record(name, phone)
#         return addressbook.add_rec(rec)



# artem = AddressBook()
# # print(artem.addressbook)
# print(artem.add_record('artem'))
ira = Test('ira')
print(ira.data)