
import re


def find_all_links(text):
    result = []
    iterator = re.finditer(
        r"\s(?:(?:http://www.)|(?:https://www.)|(?:http://)|(?:https://))([a-z]+\.[a-z]{3})", text)
    for match in iterator:
        result.append(match.group().lstrip())
    return result


text = 'The advertisements https://www.google.com are provided by Carbon, but implemented by regex101. '\
    'No cookies  https://www.facebook.com will be used for tracking http://github.comand no third party scripts will be loaded.'

print(find_all_links(text))

"""
The advertisements https://www.google.com are provided by Carbon, but implemented by regex101.
No cookies  https://www.facebook.com will be used for tracking http://github.comand no third party scripts will be loaded.


    Початок гіперпосилання може бути http:// або https://
    доменне ім'я — це набір латинських букв, цифр, символів підкреслення _ та точок .
    символи точок . не можуть зустрічатися поруч

https://www.google.com
https://www.facebook.com
https://github.com
"""
