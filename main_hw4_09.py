def is_valid_pin_codes(pin_codes):

    copy_pin = set(pin_codes)

    if len(pin_codes) <= 1 or pin_codes == ['']:
        return False
    elif len(copy_pin) != len(pin_codes):
        return False
    else:
        for i in pin_codes:
            if len(i) != 4:
                return False

            for num in i:
                if ord(num) > 57 or ord(num) < 48:
                    return False
        return True


user = list(['1234', '5678', '9123', '5678', '9123'])


result = is_valid_pin_codes(user)
print(result)
