def all_sub_lists(data):
    quantity = 0
    result_list = []
    temp_list = []
    result_list.append(temp_list)
    for i in data:
        quantity += 1
    # for i in data:
    #     result_list.append(i)
    # qu2 = len(data)
    # print(quantity, qu2)
    for i in range(quantity):
        for k in range(i, quantity):
            temp_list = data[i:k+1]
            result_list.append(temp_list)

    return sorted(result_list, key=len)


list_test = [1, 2, 3, 4]

print(all_sub_lists(list_test))
"""


Підсписком (sublist) називають список, що є складовою більшого списку. 
Підсписок може містити один елемент, множину елементів або бути порожнім.

Наприклад, [1], [2], [3] та [4] є підсписками списку [1, 2, 3, 4]. 
Список [2, 3] також входить до складу [1, 2, 3, 4], але при цьому список [2, 4] 
не є підсписком [1, 2, 3, 4], оскільки у вихідному списку числа 2 і 4 не є сусідами.

Порожній список є підсписком будь-якого списку.

Напишіть функцію all_sub_lists, що повертає список, який містить всі можливі підсписки заданого.

Наприклад, якщо функції передано аргумент список [1, 2, 3], то функція має повернути 
наступний список: [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]].

Функція all_sub_lists повинна повертати щонайменше один список з порожнім підсписком [[]].


"""
