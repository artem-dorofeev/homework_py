# txt = "sun"
# my_table = txt.maketrans("u", "o")

# # txt = "sun"
# # my_table = txt.maketrans("nus", "mot")
# # print(txt.translate(my_table))

# # txt = "the sun"
# # my_table = txt.maketrans("nus", "nos", "he t")

# print(txt.translate(my_table))
# print(my_table)


# CYRILLIC = ("а", "ч", "ш")
# LATIN = ("a", "ch", "sh")

# TRANSLIT_DICT = {}

# for c, l in zip(CYRILLIC, LATIN):
#     TRANSLIT_DICT[ord(c)] = l
#     TRANSLIT_DICT[ord(c.upper())] = l.upper()

# print(f'чаша {"чаша".translate(TRANSLIT_DICT)}')
# print("ЧАША".translate(TRANSLIT_DICT))

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
CYRILLIC = []

for i in CYRILLIC_SYMBOLS:
    CYRILLIC.append(i)

for c, l in zip(CYRILLIC, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()




def translate(name):
    global TRANS
    return name.translate(TRANS)


text = 'Дорофеев Артем Павлович на работе шото делает'
print(translate(text))


# print(type(CYRILLIC_SYMBOLS))
# print(type(TRANSLATION))
# print(type(CYRILLIC))
# print(TRANSLATION)
# print(CYRILLIC)
# print(TRANS)
# print("Артем Павлович Дорофеев".translate(TRANS))