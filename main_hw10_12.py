class IDException(Exception):
    pass


def add_id(id_list, employee_id):

    return None


# test_str = "ksgfj 7 kjs 888 shgjhsg 99 lslgn2"
# result = NumberString(test_str)
# print(result.number_count())
# test_str = NumberString('w1w1w222')
# result = test_str.number_count()
# print(result)
"""

Створіть клас IDException, який успадковуватиме клас Exception.

Також реалізуйте функцію add_id(id_list, employee_id), яка додає до списку id_list 
ідентифікатор користувача employee_id та повертає вказаний оновлений список id_list.

Функція add_id буде викликати власне виключення IDException, якщо employee_id не 
починається з '01', інакше employee_id буде додано до списку id_list.


"""
