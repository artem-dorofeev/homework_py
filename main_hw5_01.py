def real_len(text):
    len_text = 0

    if text.find("\n") > 0:
        len_text += 1
    if text.find("\v") > 0:
        len_text += 1
    if text.find("\t") > 0:
        len_text += 1
    if text.find("\r") > 0:
        len_text += 1
    if text.find("\f") > 0:
        len_text += 1

    return len(text) - len_text


test_text = 'Alex\nKdfe23\t\f\v.\r'
test_text2 = 'AlexKdfe23.'

print(real_len(test_text))

# print(test_text)
# print(test_text.find("es"))
# print(test_text.find("\n"))

# symb = test_text.find("\n")
# print(symb)

print(len(test_text))
# print(len(test_text2))

len_text = 0

# len_text += 1 if test_text.find("\n") > 0

if test_text.find("\n") > 0:
    len_text += 1
if test_text.find("\v") > 0:
    len_text += 1
if test_text.find("\t") > 0:
    len_text += 1
if test_text.find("\r") > 0:
    len_text += 1
if test_text.find("\f") > 0:
    len_text += 1

print(len(test_text) - len_text)


# line_feed = text.find("\n")  # \n
# line_tab = text.find("\v")  # \v
# char_tab = text.find("\t")  # \t
# carriage_return = text.find("\r")  # \r
# form_feed = text.find("\f")  # \f
# text_len = len(text)
