def total_salary(path):
    fh = open(path, 'r')
    result = 0

    while True:
        line = fh.readline()
        if not line:
            break
        temp_line = line.strip().split(',')
        result += float(temp_line[1])

    fh.close()
    return result


result = total_salary('cash.txt')
print(result)
print(type(result))

"""
Приклад файлу:

Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000

Як бачимо, структура файлу – це прізвище розробника та значення його заробітної плати, розділеної комою.

Розробіть функцію total_salary(path) (параметр path - шлях до файлу), яка буде розбирати текстовий файл і повертати загальну суму заробітної плати всіх розробників компанії.

Вимоги до завдання:

    функція total_salary повертає значення типу float
    для читання файлу функція total_salary використовує лише метод readline
    ми поки що не використовуємо менеджер контексту with

"""
