from datetime import date


def get_days_in_month(month, year):

    list_day = (31, 30, 29, 28)
    for i in list_day:
        try:
            result = date(year, month, i)
            break
        except ValueError:
            continue

    return result.day


# test_list = '2020-10-09'
# result = get_days_in_month(2, 2023)
print(get_days_in_month(2, 2023))


"""

Напишіть функцію визначення кількості днів у конкретному місяці. 
Ваша функція повинна приймати два параметри: month - номер місяця у вигляді цілого числа в діапазоні 
від 1 до 12 і year - рік, що складається із чотирьох цифр. Перевірте, чи функція коректно обробляє місяць лютий високосного року.


"""
