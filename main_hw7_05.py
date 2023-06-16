def capital_text(s):
    list_text = s.strip()
    list_text = list_text[0].upper() + list_text[1:]
    num_item = len(list_text)
    new_list = ''

    i = 0
    while i <= num_item - 1:
        if list_text[i] == '.' and num_item > i + 2 and list_text[i + 1] == ' ':
            new_list += list_text[i] + ' ' + list_text[i+2].upper()
            i += 2
        elif list_text[i] == '!' and num_item > i + 2 and list_text[i + 1] == ' ':
            new_list += list_text[i] + ' ' + list_text[i+2].upper()
            i += 2
        elif list_text[i] == '?' and num_item > i + 2 and list_text[i + 1] == ' ':
            new_list += list_text[i] + ' ' + list_text[i+2].upper()
            i += 2
        else:
            new_list += list_text[i]
        i += 1
    return new_list


umova = ' jfhg dflhkjd. vnvn? kjfhdfh fbdlfb! fdl;dghj.   '


result = capital_text(umova)

print(result)
print(umova)

# це виконання від ментора
# def capital_text(s):
#     s = s.strip().capitalize()
#     next_capital = False
#     result = ''
#     for ch in s:
#         if ch in ["!", ".", "?"]:
#             next_capital = True
#         if ch.isalpha() and next_capital:
#             ch = ch.upper()
#             next_capital = False
#         result += ch
#     return result

# p = re.sub(r'\.\ [a-z]', 'TTT', umova)
# print(p)

# for i in list_test:


"""
    Функція повинна:

    зробити великою першу літеру в рядку, попри прогалини
    зробити великою першу літеру після точки, попри прогалини
    зробити великою першу літеру після знака оклику, попри прогалини
    зробити великою першу літеру після знака питання, попри прогалини


"""
