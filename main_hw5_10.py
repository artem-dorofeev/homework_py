import re


def find_word(text, word):
    search_str = re.search(word, text)

    if search_str:
        index = search_str.span()
        result = {'result': True,
                  'first_index': index[0],
                  'last_index': index[1],
                  'search_string': search_str.group(),
                  'string': search_str.string}
    else:
        result = {'result': False,
                  'first_index': None,
                  'last_index': None,
                  'search_string': word,
                  'string': text}
    return result


text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Pytho 0.9.0."
word = "pythot"

# test = re.search(word, text)
# print(test)

find_word(text, word)
# print(test.group())
# print(test.span())
# print(test.string)

# test2 = test.span()
# print(test2[0])

# for e in text:
#     match_list = re.match(r"\w+", e)
#     if e:
#         print(match_list)


# result = re.search(word, text)

# print(result)
# print(type(result))

# s = "I am 25 years old."
# age = re.search('\d+', s)
# print(age.group())
