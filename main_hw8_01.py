from datetime import datetime


def get_days_from_today(date):
    if not date:
        return None
    date_list = date.split('-')
    date_start = datetime(int(date_list[0]), int(
        date_list[1]), int(date_list[2])).date()
    current_datetime = datetime.now().date()
    result = current_datetime - date_start
    return result.days


test_list = '2020-10-09'
result = get_days_from_today(test_list)
print(result)


"""


Розробіть функцію get_days_from_today(date), яка повертатиме кількість днів від поточної дати, де параметр date - це рядок формату '2020-10-09' (рік-місяць-день).

Підказки:

    Параметр date розбити на рік, місяць та день можна використовуючи метод рядків split.
    datetime приймає аргументи типу int, використовуйте перетворення типів.
    ігноруйте години, хвилини та секунди для вашої дати, важливі повні дні.
    кількість днів ви можете отримати відніманням з поточної дати, заданої в змінній date (без часу).

Наприклад: Якщо поточна дата - '5 травня 2021', то виклик get_days_from_today("2021-10-09") поверне нам -157.


"""
