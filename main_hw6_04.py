def add_employee_to_file(record, path):
    file = open(path, 'a')
    file.write('\n' + record)
    file.close()


# def write_employees_to_file(employee_list, path):
#     fh = open(path, 'w')
#     for item in employee_list:
#         for i in item:
#             # i += '\n'
#             fh.write(i + '\n')

#     fh.close()
piople = 'Artem Dorofeev, 44'

add_employee_to_file('Drake Mikelsson,19', 'cash.txt')
fh = open('cash.txt', 'r')

print(fh.read())


fh.close()


"""


Реалізуйте функцію add_employee_to_file(record, path), яка у файл (параметр path - шлях до файлу) буде додавати співробітника (параметр record) у вигляді рядка "Drake Mikelsson,19".

Вимоги:

    параметр record - співробітник у вигляді рядка виду "Drake Mikelsson,19"
    кожен запис у файл має починатися з нового рядка.
    необхідно щоб стара інформація у файлі теж зберігалася, тому при роботі з файлом відкрийте файл у режимі 'a', додайте співробітника record у файл і закрийте його
    ми поки що не використовуємо менеджер контексту with



"""
