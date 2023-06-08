def get_credentials_users(path):
    list = []
    with open(path, 'rb') as file:
        while True:
            line = file.readline().decode()
            if not line:
                break
            list.append(line.rstrip())

    return list


sourse = 'raw_data6_11.bin'
result = get_credentials_users(sourse)
print(result)


"""

Реалізуйте функцію get_credentials_users(path), яка повертає список рядків із бінарного файлу, створеного в попередньому завданню, де:

    path – шлях до файлу.

Формат файлу:

andry:uyro18890D
steve:oppjM13LL9e

Відкрийте файл для читання, використовуючи with та режим rb. Сформуйте список рядків із файлу та поверніть його з функції get_credentials_users у наступному форматі:

['andry:uyro18890D', 'steve:oppjM13LL9e']

Вимоги:

    Використовуйте менеджер контексту для читання з файлу



"""
