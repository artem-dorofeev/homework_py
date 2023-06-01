import re


# def find_word(text, word):


text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
word = "Python"

for e in text:
    match_list = re.match(r"\w+", e)
    if e:
        print(match_list)


# result = re.search(word, text)

# print(result)
# print(type(result))
