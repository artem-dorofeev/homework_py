# def flatten(data):
#     result_list = []

#     if len(data) == 0:
#         return result_list

#     for i in data:
#         if type(i) == list:
#             flatten(i)
#         else:
#             result_list.append(i)

#     return result_list


# test_list = [1, 2, [3, 4, [5, 6]], 7]
# test_list2 = [1, 2, 5, 7]
# result = flatten(test_list)
# print(result)


def flatten(data):
    lis_out = []
    if data == []:
        lis_out = []
        return lis_out
    if type(data[0]) == list:
        first_list = flatten(data[0])
        second_list = flatten(data[1:])
        lis_out = first_list + second_list
    if type(data[0]) != list:
        first_list = data[:1]
        second_list = flatten(data[1:])
        lis_out = first_list + second_list
    return lis_out


test_list = [1, 2, [3, 4, [5, 6]], 7]
test_list2 = [1, 2, 5, 7]
result = flatten(test_list)
print(result)


"""


Рекурсія добре підходить до задачі flatentening. Це процес вирівнювання списків, який полягає в позбавленні вкладеної структури. Наприклад список вигляду [1, 2, [3, 4, [5, 6]], 7] має бути перетворений на плоский (flat) список [1, 2, 3, 4, 5, 6, 7]

Напишіть функцію flatten, яка приймає на вхід список, рекурсивно вирівнюватиме цей список і повертатиме пласку версію списку.

Для виконання завдання можна дотримуватися наступного алгоритму:

Якщо вхідний список порожній, то:
  Повертаємо порожній список
Якщо перший елемент списку є списком, то:
  Отримуємо перший список, рекурсивно викликавши функцію з першим елементом списку
  Отримуємо другий список, рекурсивно викликавши функцію з рештою списку без першого елемента
  Повертаємо конкатенацію двох списків
Якщо перший елемент списку не є списком, то:
  Отримуємо перший список із першого елемента списку
  Отримуємо другий список, рекурсивно викликавши функцію з рештою списку без першого елемента
  Повертаємо конкатенацію двох списків




"""
