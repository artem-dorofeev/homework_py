from collections import UserDict
from normalize_phone import normalize_phone

COMMAND_EXIT = ['good bye', 'close', 'exit']
contacts_dict = [{"name": "Artem", "phone": "+380504848484"},
                 {"name": "Ira", "phone": "+380501111111"},
                 {"name": "Diana", "phone": "+380502222222"},]

COMMAND_DICT = {
    hello_func: "hello",
    add_func: "add",
    show_all: "show all",
    change_contact: "change",
    phone_print: "phone"
}


from collections import UserDict
    
    
class Field:
    def __init__(self, value) -> None:
        self.value = value
                
class Name(Field):
    pass
   
class Phone(Field):
    pass
      
class Record():
    def __init__(self, name:Name, phone:Phone=None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

class AddressBook(UserDict):
    def add_record(self, rec:Record):
        self.data[rec.name.value] = rec
        print(self)


def select_command(text):
    for key, val in COMMAND_DICT.items():
        if val == text:
            return key
    return f'non command in list'


def parser_text(text):
    text = text.lower().strip()
    if text.startswith("show all"):
        return "show all", None
    else:
        user_text = text.split()
        return user_text[0], user_text[1:]


def main():

    while True:

        user_input = input('>>input>>')
        if user_input.lower().strip() in COMMAND_EXIT:
            print('Good bye!')
            break
        user_command, other_text = parser_text(user_input)
        result = select_command(user_command)
        if type(result) == str:
            print(result)
        else:
            print(result(other_text))


if __name__ == "__main__":
    main()

    # artem = AddressBook()
    # # # print(artem.addressbook)
    # # print(artem.add_record('artem'))
    # ira = Test('ira')
    # print(ira.data)
