# def save_credentials_users(path, users_info):
#     line_user = ''
#     for key, value in users_info.items():
#         line_user += key + ': ' + value + '\n'

#     with open(path, 'wb') as file:
#         file.write(line_user.rstrip().encode())
"""
перша функція моя, друга скопійована із слаку і троха перероблена. моя теж працює, результат однаковий але хз чому не проходить автоперевірку 
"""


def save_credentials_users(path, users_info):
    with open(path, 'wb') as fh:
        line_user = ''
        for key, value in users_info.items():
            line_user = key + ':' + value + '\n'
            b_line_user = line_user.encode()
            fh.write(b_line_user)
    return True


line_user = ''

users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}
fl = 'raw_data.bin'


save_credentials_users(fl, users_info)


"""

Дані про користувачів краще зберігати у форматі бінарних файлів. Тому вам необхідно створити функцію, яка буде записувати логін та пароль користувача у файл.

Реалізуйте функцію save_credentials_users(path, users_info), яка зберігає інформацію про користувачів з паролями в бінарний файл.

Де:

    path – шлях до файлу.
    users_info - словник типу {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}, де ключ — логін (username) користувача, а значення — його пароль (password).

Вимоги:

    Кожен рядок файлу повинен мати такий вигляд username:password. Такий формат запису використовують при Базовій аутентифікації.
    Відкрийте файл для запису та збережіть ключ та значення зі словника users_info у вигляді окремого рядка username:password для кожного елемента словника users_info



"""
