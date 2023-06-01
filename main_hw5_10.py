import re


# def find_word(text, word):


text = "Guido van Rossum began working on Pytho in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Pytho 0.9.0."
word = "Python"

test = re.search(word, text)
print(test)
# print(test.group())
print(test.span())
print(test.string)

test2 = test.span()
print(test2[0])

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
