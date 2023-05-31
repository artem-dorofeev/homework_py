def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()

    result = False

    for spam in spam_words:
        spam = spam.lower()

        if space_around:
            new_text = (
                text.strip()
                .replace(".", "")
                .replace(",", "")
            )

            for i in new_text.split(" "):
                if i == spam:
                    result = True
                    break

        if text.find(spam) >= 0 and space_around == False:
            result = True
            break

    return result


text_str = 'Передбачити третій параметр функції space_around, який за замовчуванням дорівнює False. '

sp_text = ('sddd', 'trtr', 'Fals')

print(is_spam_words(text_str, sp_text))
