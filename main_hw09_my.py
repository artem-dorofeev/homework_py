
COMMAND_EXIT = ['good bye', 'close', 'exit']
contacts_dict = [{"name": "Artem", "phone": "+380504848484"},
                 {"name": "Ira", "phone": "+380501111111"},
                 {"name": "Diana", "phone": "+380502222222"},]


def format_phone_number(func):
    def wrapper(x):
        result = func(x)
        if len(result) == 12:
            result = '+' + result
        else:
            result = '+38' + result
        return result
    return wrapper


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def hello_func(text=None):
    return f'How can I help you?'


def add_func(text):
    global contacts_dict
    if len(text) < 2:
        return f'name or phone unknow format'
    name = text[0].capitalize()
    phone = sanitize_phone_number(text[1])
    new_contact = {"name": name, "phone": phone}
    contacts_dict.append(new_contact)
    return f'add contact {name} - {phone}'


def show_all(text=None):
    result = 'Contacts list \n'
    for i in contacts_dict:
        result += 'name ' + i["name"] + ' phone ' + i["phone"] + "\n"
    return result


def change_contact(list_contacts):
    global contacts_dict
    if len(list_contacts) < 2:
        return f'name or phone unknow format'
    name = list_contacts[0].capitalize()
    phone = sanitize_phone_number(list_contacts[1])
    for i in contacts_dict:
        if i["name"] == name:
            i["phone"] = phone
            return f'contast {i["name"]} take new phone {i["phone"]}'
    return f'Not {name} in contact list'


def phone_print(name):
    contact = name[0].capitalize().strip()
    for i in contacts_dict:
        if i["name"] == contact:
            return f'name: {contact} phone: {i["phone"]}'
    return f'Not {contact} in contact list'


COMMAND_DICT = {
    hello_func: "hello",
    add_func: "add",
    show_all: "show all",
    change_contact: "change",
    phone_print: "phone"
}


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
