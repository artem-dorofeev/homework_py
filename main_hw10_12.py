class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if not employee_id.startswith('01'):
        raise IDException
    else:
        id_list.append(employee_id)

    return id_list


test_str = 'test str'
# if not test_str.startswith('te'):
#     print('yes')
# else:
#     print('no')
id_list = ['mmm', 'bbbb']
result = add_id(id_list, test_str)
print(result)

"""

Створіть клас IDException, який успадковуватиме клас Exception.

Також реалізуйте функцію add_id(id_list, employee_id), яка додає до списку id_list 
ідентифікатор користувача employee_id та повертає вказаний оновлений список id_list.

Функція add_id буде викликати власне виключення IDException, якщо employee_id не 
починається з '01', інакше employee_id буде додано до списку id_list.


"""
