from random import randrange


def get_numbers_ticket(min, max, quantity):
    result = []
    if min < 1 or max > 1000 or quantity < min or quantity > max:
        return result
    while len(result) < quantity:
        item = randrange(min, max)
        if item not in result:
            result.append(item)

    result.sort()
    return result


min = 1
max = 10
quantity = 8

result = get_numbers_ticket(min, max, quantity)
print(result)


"""
Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим 
чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

Напишіть функцію, яка випадково підбиратиме набір чисел для лотерейного квитка. Серед цих чисел не має бути дублікатів.

Формат функції get_numbers_ticket(min, max, quantity), де параметри:

    min - мінімальне значення діапазону, не може бути менше 1
    max - максимальне значення діапазону, не може бути більше 1000
    quantity - кількість чисел у наборі (має бути min < quantity < max)

Функція повинна повернути перелік випадкових чисел за зростанням. Якщо порушено умови обмежень на параметри функції, тоді повернути пустий список
"""
