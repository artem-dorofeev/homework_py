def make_request(keys, values):
    result_dict = {}
    if len(keys) != len(values):
        return result_dict
    k = 0
    while k < len(keys):
        result_dict[keys[k]] = values[k]

        k += 1

    return result_dict


list_keys = [1, 2, 3, 4]
list_values = ['one', 'dou', 'start', 'finish']

print(make_request(list_keys, list_values))
"""

При роботі веб-сервісів спілкування, за протоколом HTTP, найчастіше відбувається в форматі JSON.
 І надсилання даних на сервер при запиті POST - це необхідність використовувати словник, 
 оскільки структура формату JSON ідентична словнику Python.

Реалізуйте допоміжну функцію, яка формуватиме запит на сервер у вигляді словника. 
Дана функція make_request(keys, values) приймає два параметри у вигляді списків. 
Функція повинна створити словник із ключами з списку keys та значеннями зі списку values.

    Порядок відповідності збігається з індексами списків keys та values.
    Якщо довжина keys та values не збігаються, поверніть порожній словник.


"""
