import re


def find_all_words(text, word):
    return re.findall(word, text, flags=re.IGNORECASE)


all_text = 'function of re in python will search the regular expression pattern and return the first occurrence. The Python RegEx Match method checks for a match only at the beginning of the string. So, if a match is found in the first line, it returns the match object. But if a match is found in some other line, the Python RegEx Match function returns null.'
word = 'Python'

# result = re.findall(word, all_text, flags=re.IGNORECASE)

# print(result)

print(find_all_words(all_text, word))
