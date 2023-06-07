def save_applicant_data(source, output):
    st_list = []
    for i in source:
        st_str = i.get('name') + ',' + str(i.get('specialty')) + ',' + \
            str(i.get('math')) + ',' + \
            str(i.get('lang')) + ',' + str(i.get('eng')) + '\n'
        st_list.append(st_str)

    print(st_list)
    with open(output, "w") as file:
        file.writelines(st_list)


list_st = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
output = 'hw6_08_out.txt'

save_applicant_data(list_st, output)

# # print(list_st)

# for i in list_st:
#     # lis_st = '{}, {}, {}, {}, {}'.format(i.get('name'), i.get(
#     #     'specialty'), i.get('math'), i.get('lang'), i.get('eng'))
#     # print(list_st)
#     list_str = i.get('name') + ',' + str(i.get('specialty')) + ',' + \
#         str(i.get('math')) + ',' + str(i.get('lang')) + ',' + str(i.get('eng'))
#     print(list_str)
#     # s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
#     for key, value in i.items():
#         print(key, value)
# print(i)
# new_str = ''
# for val in i.values():
#     new_str += str(val)
#     new_str += ','
# print(new_str)

"""
У кожному словнику цього списку записано прізвище абітурієнта — ключ name, код спеціальності, на яку він поступив — ключ specialty, та отримані ним бали з окремих дисциплін — ключі math (математика), lang ( українська мова) та eng (англійська мова)

Розробіть функцію save_applicant_data(source, output), яка буде вказаний список із параметра source зберігати у файл із параметра output

Структура файлу для зберігання повинна бути наступною. У кожному новому рядку файлу повинні бути записані через кому без прогалин прізвище абітурієнта, код спеціальності, на яку він поступив, та отримані ним бали за окремими дисциплінами.

Kovalchuk Oleksiy,301,175,180,155
Ivanchuk Boryslav,101,135,150,165
Karpenko Dmitro,201,155,175,185

Вимоги:

    відкрийте файл output для запису, використовуючи менеджер контексту with та режим w.
    запис нового вмісту файлу output має бути або за допомогою методу writelines, або використовувати метод write

"""
