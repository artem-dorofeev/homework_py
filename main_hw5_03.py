def sanitize_phone_number(phone):
    # phone = phone = phone.strip()
    new_list = ''

    for i in phone:
        if i != "(" and i != ")" and i != "+" and i != "-" and i != " ":
            new_list += i

    return new_list


phone = "38050 111 22 11   "
result = sanitize_phone_number(phone)
print(result)
