def sanitize_file(source, output):
    new_list = ''
    map = {ord('9'): '', ord('8'): '', ord('7'): '', ord('6'): '', ord(
        '5'): '', ord('4'): '', ord('3'): '', ord('2'): '', ord('1'): '', ord('0'): ''}
    with open(source, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            new_list += line.translate(map)

    file = open(output, "w")
    file.write(new_list)
    file.close


source = 'hw6_07_in.txt'
output = 'hw6_07_out.txt'

sanitize_file(source, output)


# map = {ord('9'): '', ord('8'): '', ord('7'): '', ord('6'): '', ord(
#     '5'): '', ord('4'): '', ord('3'): '', ord('2'): '', ord('1'): '', ord('0'): ''}
# text1 = 'jhfkj1234567890 .dldhklk;ldh; 396036 dfdkjh;a;lds 0320924 asdfh7f6s5s4a3a'
# translated = text1.translate(map)
# print(translated)

# text = "hjhfg889 lkskdfjg87 87 lksjdlk324 kgkg1"
# new_text = (text.replace("9", "")
#             .replace("8", ""))
# print(new_text)


"""

Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст текстового файлу source, очищений від цифр.

Вимоги:

    прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
    запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
    запис нового вмісту файлу output має бути одноразовий і використовувати метод write


"""
