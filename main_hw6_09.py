def is_equal_string(utf8_string, utf16_string):
    utf8 = utf8_string.decode('utf-8')
    utf16 = utf16_string.decode('utf-16')
    return utf8.casefold() == utf16.casefold()


s = "ПРивіт! Світ, цу паЙтОн!!"
s2 = "ПРивіт! Світ, цу ПаЙтОн!!"

utf8 = s.encode()
utf16 = s2.encode('utf-16')

result = is_equal_string(utf8, utf16)
print(result)


"""


Є два рядки у різних кодуваннях - "utf-8" та "utf-16". Нам необхідно зрозуміти, чи дорівнюються рядки між собою.

Реалізуйте функцію is_equal_string(utf8_string, utf16_string), яка повертає True, якщо рядки дорівнюють собі, і False — якщо ні.

"""
