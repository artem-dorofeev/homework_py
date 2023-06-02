import re


def replace_spam_words(text, spam_words):
    for i in spam_words:
        result = re.sub(i, '*' * len(i), text, flags=re.IGNORECASE)
        text = result

    return result


all_text = 'function of re in python will search the regular expression pattern' \
    'and return the first occurrence. The Python RegEx Match method checks for'


word_list = ['Python', 'first', 'search']


print(replace_spam_words(all_text, word_list))

"""У шостій задачі ми писали функцію is_spam_words, яка визначала, чи є чи ні стоп-слова у тексті повідомлення. 
Підемо далі та застосуємо функцію sub модуля re для заміни вказаних у списку стоп-слів на деякий шаблон. 
Наприклад, всі "погані" слова замінюватимемо зірочками. Напишіть функцію replace_spam_words, яка приймає 
рядок (параметр text), перевіряє його на вміст заборонених слів зі списку (параметр spam_words), 
та повертає результат рядок, але замість заборонених слів, підставлений шаблон з *, причому довжина шаблону 
дорівнює довжині забороненого слова. Визначити нечутливість до регістру стоп-слів.
"""
