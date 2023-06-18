def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as file:
        file.write(additional_info)

    with open(path, 'r') as file:

        file.seek(start_pos)
        result = file.read()[0:count_chars]

    return result


info = "test file - hello word"
path = 'D:\\test\\test_py.txt'
count = 7
start = 15
result = file_operations(path, info, start, count)


print(result)


# file_operations(path, additional_info, start_pos, count_chars)
"""


Реалізуйте функцію file_operations(path, additional_info, start_pos, count_chars), яка додає додаткову інформацію в файл на шляху path з параметра additional_info, і після цього повертає рядок з позиції start_pos довжиною count_chars.

Вимоги:

    функція повинна відкривати файл за допомогою with за шляхом path в режимі додавання інформації
    записувати в кінець файлу рядок additional_info
    після запису функція має відкрити той самий файл для читання
    прочитати та повернути рядок з позиції start_pos завдовжки count_chars за допомогою функції seek.

Важливо: для проходження завдання необхідно використовувати менеджер контексту with, методи seek, write та read.


"""
