def to_indexed(source_file, output_file):
    str_prof = ''
    with open(source_file, 'r') as file:
        count = 0
        while True:
            line = file.readline()
            if not line:
                break
            str_prof += str(count) + ': ' + line
            count += 1

    with open(output_file, 'w') as file:
        file.write(str_prof)


path = 'D:\\test\\test2_py.txt'
path_out = 'D:\\test\\test3_py.txt'

to_indexed(path, path_out)


# print(result)


"""


Напишіть функцію to_indexed(source_file, output_file), яка зчитуватиме вміст файлу, 
додаватиме до прочитаних рядків порядковий номер і зберігати їх у такому вигляді у новому файлі.

Кожний рядок у створеному файлі повинен починатися з його номера, двокрапки та пробілу, після чого має йти текст рядка з вхідного файлу.

Нумерація рядків іде від 0.


"""
