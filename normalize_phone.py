def normalize_phone(phone):
    new_phone = ''
    for i in phone:
        if 48 <= ord(i) <= 57:
            new_phone += i
    if len(new_phone) == 10:
        new_phone = '+38' + new_phone
    elif len(new_phone) == 12:
        new_phone = '+' + new_phone
    else:
        return f'unknow format phone'

    return new_phone


# def main():
#     return None


if __name__ == "__main__":
    phone = input(">>>")

    print(normalize_phone(phone))
    # main()
