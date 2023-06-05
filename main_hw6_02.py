def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    for item in employee_list:
        for i in item:
            # i += '\n'
            fh.write(i + '\n')

    fh.close()


list_piople = [['Robert Stivenson,50', 'Alex Denver,20'], ['Drake Mikelsson,100'], [
    'Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']]


write_employees_to_file(list_piople, 'test.txt')
fh = open('test.txt', 'r')

print(fh.read())


fh.close()


"""
Функція запису в файл write_employees_to_file(employee_list, path), де:

    path – шлях до файлу.
    employee_list - список зі списками співробітників по кожному відділу, як у прикладі нижче:

[['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]

Вимоги:

    запишіть вміст employee_list у файл, використовуючи режим "w".
    ми поки що не використовуємо менеджер контексту with
    кожен співробітник повинен бути записаний з нового рядка — тобто для попереднього списку вміст файлу має бути наступним:

Robert Stivenson,28
Alex Denver,30
Drake Mikelsson,19

"""
