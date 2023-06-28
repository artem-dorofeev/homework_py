import re


def generator_numbers(string=""):
    only_number = re.findall(r"\d+", string)
    list_cash = []
    for i in only_number:
        list_cash.append(int(i))

    # result2 = []
    # temp_num = ''
    # for i in string:
    #     if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
    #         temp_num += i
    #     else:
    #         if temp_num != '':
    #             result2.append(temp_num)
    #             temp_num = ''
    # print(result2)

    i = 0
    while i < len(list_cash):
        # print(result[i])
        result = yield list_cash[i]
        i += 1
    return result


def sum_profit(string):
    result = generator_numbers(string)
    summ = 0
    # for i in result:
    #     summ += i

    # print(summ)

    return summ


profit = 'The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000.'

profit2 = 'gfg 12 99'
# result = generator_numbers(profit)
sum_profit(profit)

# print(result)
# result2 = sanitize_phone_number(phone_num2)
# print(result2)

"""


Нехай є рядок з числами (з метою спрощення числа лише цілі), що визначає якісь частини загального доходу. Наприклад,

"The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."

Необхідно реалізувати функцію generator_numbers, яка буде парсити рядок і знаходити всі цілі числа в ньому та працювати як генератор, 
який буде віддавати зазначені числа при зверненні до нього у циклі.

    З парсингом рядків ми вже зіштовхувалися виконуючи завдання модуля 7, коли розбивали на лексеми арифметичний вираз

Функція generator_numbers(string="") безпосередньо розпарсює рядок і за допомогою yield повертає поточне число.

Функція sum_profit(string) підсумовує числа, отримані від generator_numbers, та повертає загальну суму прибутку з рядка.


"""
