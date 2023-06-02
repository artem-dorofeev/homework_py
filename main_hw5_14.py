import re


# def find_all_phones(text):
#     # find1 = r"\+\d{3}\(\d{2}\)\d{3}\-\d{1}\-\d{3}"
#     # find2 = r"\+\d{3}\(\d{2}\)\d{3}\-\d{2}\-\d{2}"
#     result = re.findall(
#         r"(\+\d{3}\(\d{2}\)\d{3}\-)(\d{1}\-\d{3})|(\d{2}\-\d{2})", text)
#     return result

def find_all_phones(text):
    result = re.findall(
        r"(\+\d{3}\(\d{2}\)\d{3}\-(?:(?:\d{2}\-\d{2})|(?:\d{1}\-\d{3}){1}))", text
    )
    return result


phone_list = 'Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787'

print(find_all_phones(phone_list))

"""
 ['+380(67)777-7-771', '+380(67)777-77-77', '+380(67)777-77-78']

 (\+\d{3}\(\d{2}\)\d{3}\-)(\d{1}\-\d{3})|(\d{2}\-\d{2})
 """
