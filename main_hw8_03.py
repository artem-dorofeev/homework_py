from datetime import datetime


def get_str_date(date):
    date_new = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f%z')
    return date_new.strftime('%A %d %B %Y')


test_list = '2021-05-27 17:08:34.149Z'

print(get_str_date(test_list))


"""
Напишіть функцію get_str_date(date), яка перетворюватиме дату з бази даних у форматі ISO '2021-05-27 17:08:34.149Z' 
у вигляді наступного рядка 'Thursday 27 May 2021' - день тижня, число, місяць та рік. Перетворене значення функція повертає під час виклику.

"""
