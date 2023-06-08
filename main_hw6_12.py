import base64


def encode_data_to_base64(data):
    base64_list = []
    for i in data:
        str_bytes = i.encode("utf-8")
        str64_bytes = base64.b64encode(str_bytes)
        base64_list.append(str64_bytes.decode("utf-8"))

    return base64_list


list = ['andry:uyro18890D', 'steve:oppjM13LL9e']
result = encode_data_to_base64(list)
print(result)
# encode_data_to_base64(list)

"""
Функція get_credentials_users із попереднього завдання повертає нам список рядків username:password:

['andry:uyro18890D', 'steve:oppjM13LL9e']

Реалізуйте функцію encode_data_to_base64(data), яка приймає у параметрі data зазначений список, виконує кодування кожної пари username:password у формат Base64 та повертає список із закодованими парами username:password у вигляді:

['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']

Приклад:

import base64

message = "Hello world!"
message_bytes = message.encode("utf-8")
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode("utf-8")

print(base64_message)  # SGVsbG8gd29ybGQh


"""
