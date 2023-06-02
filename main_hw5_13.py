import re


def find_all_emails(text):
    result = re.findall(
        r"[A-Za-z]{1}[A-Za-z0-9._]{1,}@[A-Za-z]+\.[A-Za-z]{2,}", text)
    return result


# # text = 'Here we have a a.dorof@uu.ee list of e-mail addresses, ' \
#     'and jdgfksg@fdgj.wqq we want all the e-mail addresses hgj_gf@hdgs.tdt to be ' \
#     'fetched out a@assd.com from the list, we use the method re.findall() in Python. It will find all the e-mail addresses from the list.'
text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'


result = re.findall(r"[a-zA-Z][\w.]+@\w+.\w{2,3}", text)

print(result)
"""

Тепер ми потренуємося писати корисні регулярні вирази. Напишіть регулярний вираз для функції find_all_emails, 
яка буде в тексті (параметр text) знаходити всі email та повертати список отриманих з тексту збігів.

З метою спрощення приймемо, що: ми використовуємо для email, — англійський алфавіт префікс 
(все, що знаходиться до символу @) починається з латинської літери та може містити будь-яке число або букву, 
включаючи нижнє підкреслення та символ точки. Має складатися мінімум із двох символів
суфікс email (все, що знаходиться після символу @) складається лише з букв англійського алфавіту, та має дві частини, 
розділені точкою, також доменне ім'я верхнього рівня не може бути менш ніж два символи (все, що після точки)

Даний регулярний вираз жодною мірою не претендує на покриття всіх можливих варіантів email.

При виконанні цього завдання ми рекомендуємо використовувати наступний сервіс для перевірок регулярних виразів regex101.

"""

# "[a-zA-Z][\w.]+@\w+.\w{2,3}"g
