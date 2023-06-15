def is_integer(s):
    list_num = ''

    if len(s) == 0:
        return False

    for i in s:
        if i != ' ':
            list_num += i

    if len(list_num) == 0:
        return False

    if list_num[0] == '+' or list_num[0] == '-':
        list_num = list_num[1:]

    return list_num.isdigit() if len(list_num) >= 1 else False

    # if len(list_num) >= 1:
    #     return list_num.isdigit()


list_test = '  '
# result = is_integer(list_test)

print(is_integer(list_test))
# print(type(result))
# print(result[0])


# print(list_test)
# print(type(list_test))
# print(list_test[1])


"""
    У Python існує рядкова функція isdigit(). Ця функція повертає True, якщо всі символи в рядку є цифрами, 
    і є принаймні один символ, інакше — False. Напишіть функцію з ім'ям is_integer, яка розширюватиме функціональність isdigit(). 
    При перевірці рядка необхідно ігнорувати початкові та кінцеві прогалини в рядку. 
    Після виключення зайвих прогалин рядок вважається таким, що представляє ціле число, якщо:

    її довжина більша або дорівнює одному символу
    вона повністю складається з цифр
    передбачити виняток, що, можливо, є початковий знак "+" або "-", після якого мають йти цифри

"""
