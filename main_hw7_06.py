def solve_riddle(riddle, word_length, start_letter, reverse=False):
    result = ''
    if reverse == True:
        riddle = riddle[::-1]
    num = riddle.find(start_letter)
    if (num + word_length) <= len(riddle):
        result = riddle[num:num + word_length]
    return result


text_rebus = 'qwertyuiopasdfghjkl'
# riddle = text_rebus
# start_letter = 'm'
# word_length = 4
# reverse = False

print(solve_riddle(text_rebus, 6, 't', True))

# print(len(riddle), num)
# print(riddle)
# print(start_letter)
# print(result)


"""
Реалізуйте функцію solve_riddle(riddle, word_length, start_letter, reverse=False) для знаходження слова, що шукається в рядку ребуса.

Параметри функції:

    riddle - рядок із зашифрованим словом.
    word_length – довжина зашифрованого слова.
    start_letter - літера, з якої починається слово (мається на увазі, що до початку слова літера не зустрічається в рядку).
    reverse - вказує, у якому порядку записане слово. За замовчуванням — в прямому. Для значення True слово зашифроване у зворотньому порядку, наприклад, у рядку 'mi1rewopret' зашифроване слово 'power'.

Функція повинна повертати перше знайдене слово. Якщо слово не знайдене, повернути пустий рядок.


"""
