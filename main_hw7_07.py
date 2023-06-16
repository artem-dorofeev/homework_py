def data_preparation(list_data):
    result = []
    for i in list_data:
        quantity = 0
        for k in i:
            quantity += 1

        if quantity > 2:
            i.remove(min(i))
            i.remove(max(i))

    for i in list_data:
        result.extend(i)
    result.sort(reverse=True)

    return result


list_num = [[1, 2, 3], [4, 5, 6, 7], [3], [0], [5, 6], [9, 8, 7, 4, 3]]
result = data_preparation(list_num)
print(result)


# new_list = []
# for i in list_num:
#     new_list.extend(i)

# print(list_num)
# print(new_list)
# new_list.sort(reverse=True)
# print(new_list)
# k = 0
# for i in new_list:
#     k += 1
# print(f'quantiti new list - {k}')
# list_num = [[1, 2, 3], [4, 5, 6, 7], [3], [0], [5, 6], [9, 8, 7, 4, 3]]


"""


У четвертому модулі розв'язували завдання нормалізації даних. Розширимо її.

При аналізі даних часто виникає необхідність позбавитися екстремальних значень, перш ніж почати працювати з даними далі. 
Напишіть функцію data_preparation, яка приймає набір даних, список списків (Приклад: [[1,2,3],[3,4], [5,6]]).

Функція повинна видаляти з переданих списків найбільше і найменше значення, але якщо розмір списку понад два елементи. 
Після видалення даних з кожного списку необхідно злити їх разом в один список, відсортувати його за зменшенням та повернути 
отриманий список як результат (Для прикладу вище результат буде наступним: [6, 5, 4, 3, 2]).


"""
