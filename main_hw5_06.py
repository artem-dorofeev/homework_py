def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()
    spam_words = spam_words.lower()

    result = True if text.find(spam_words) >= 0 else False

    if space_around:
        new_text = (
            text.strip()
            .replace(".", "")
            .replace(",", "")
        )
        for i in new_text.split(" "):
            if i == spam_words:
                result = True
            else:
                result = False

    return result


text_str = 'Передбачити третій параметр функції space_around, який за замовчуванням дорівнює False. '

sp_text = 'Spa'

print(is_spam_words(text_str, sp_text))

# result = True if text_str.find(sp_text) >= 0 else False

# print(result)

# text_split = text_str.split(" ")
# print(text_split)

# new_phone = (
#     text_str.strip()
#     .removeprefix("+")
#     .replace("(", "")
#     .replace(")", "")
#     .replace(".", "")
#     .replace(",", "")
# )

# print(new_phone)

# for i in new_phone.split(" "):
#     if i == sp_text:
#         print("NASHEL")
