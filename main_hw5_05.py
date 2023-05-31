def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    jp_list = list()
    sg_list = list()
    tw_list = list()
    ua_list = list()

    for i in list_phones:
        i = sanitize_phone_number(i)
        if i.startswith("81"):
            jp_list.append(i)
        elif i.startswith("65"):
            sg_list.append(i)
        elif i.startswith("886"):
            tw_list.append(i)
        else:
            ua_list.append(i)

    result = {"UA": ua_list, "JP": jp_list, "SG": sg_list, "TW": tw_list}
    return result


phone = "38050 111 22 11   "
result = sanitize_phone_number(phone)
print(result)

list_phone = ('380-501233234', '+8105-03451234', '886-0508-8899-00',
              '+65380501112222', '+380501112211', '8(86)000', '  650707')
result = get_phone_numbers_for_countries(list_phone)
print(result)
