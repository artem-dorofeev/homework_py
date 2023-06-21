from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    dec_summ = Decimal(0)
    getcontext().prec = signs_count
    for i in number_list:
        dec_summ += Decimal(i)

    return dec_summ / len(number_list)


number_list = [31, 55, 177, 2300, 1.57]
signs_count = 9

# decimal_average(number_list, signs_count)

result = decimal_average(number_list, signs_count)
print(result)


"""

Створіть функцію decimal_average(number_list, signs_count), яка обчислюватиме середнє арифметичне типу Decimal з 
кількістю значущих цифр signs_count. Параметр number_list — список чисел

Увага
Не забувайте приводити всі числа у списку до типу `decimal`

Приклад:

    виклик функції decimal_average([3, 5, 77, 23, 0.57], 6) поверне 21.714
    виклик функції decimal_average([31, 55, 177, 2300, 1.57], 9) поверне 512.91400

"""
