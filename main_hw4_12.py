from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_num = False
    for ch in password:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_num = True
    if len(password) == 8 and has_upper and has_lower and has_num:
        return True
    return False


def get_password():
    result = False
    i = 1
    while result == False and i in range(100):
        new_pass = get_random_password()
        result = is_valid_password(new_pass)
        print(f'i > {i} pass > {new_pass} valid {result}')
        i += 1

    return new_pass if result else False


result = get_password()
print(result)
