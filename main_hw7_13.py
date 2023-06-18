def get_employees_by_profession(path, profession):

    with open(path, 'r') as file:
        str_find = file.readline()

    # with open(path, 'r') as file:

    #     file.seek(start_pos)
    #     result = file.read()[0:count_chars]

    return result


info = "test file - hello word"
path = 'D:\\test\\test_py.txt'
count = 7
start = 15
result = file_operations(path, info, start, count)


print(result)


# file_operations(path, additional_info, start_pos, count_chars)
"""
Є файл зі списком працівників компанії. У кожному рядку файлу записано інформацію лише одного співробітника. 
Формат запису, в межах навчання приймемо спрощений, такий як: ім'я співробітника, символ пропуску та його посада, тобто, ким він працює.

Створіть функцію get_employees_by_profession(path, profession). Функція повинна у файлі (параметр path) знайти всіх співробітників зазначеної професії (параметр profession)

Вимоги:

    відкрийте файл за допомогою with для читання
    отримайте рядки з файлу за допомогою методу readlines()
    за допомогою методу find знайдіть усі рядки у файлі, де є вказана profession, та помістіть записи до списку
    об'єднайте всі ці рядки в списку в один рядок за допомогою методу join (пам'ятайте про символ перенесення рядків '\n' та зайві прогалини, які треба прибрати)
    приберіть значення змінної 'profession' (замініть на порожній рядок "" методом replace)
    поверніть отриманий рядок із файлу



"""
