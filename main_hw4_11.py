# def is_valid_password(password):
#     if len(password) != 8:
#         return False
#     key = 0
#     for i in password:
#         if ord(i) >= 65 and ord(i) <= 90:
#             key += 1
#             break

#     for i in password:
#         if ord(i) >= 97 and ord(i) <= 122:
#             key += 1
#             break

#     for i in password:
#         if ord(i) >= 48 and ord(i) <= 57:
#             key += 1
#             break

#     if key != 3:
#         return False

#     print(key)
#     return True


def is_valid_password(password):

    key_upper = 0
    key_lower = 0
    key_num = 0

    # if len(password) != 8:
    #     return False

    for i in password:
        if ord(i) >= 65 and ord(i) <= 90:
            key_upper += 1

        if ord(i) >= 97 and ord(i) <= 122:
            key_lower += 1

        if ord(i) >= 48 and ord(i) <= 57:
            key_num += 1

    if key_upper == 0 or key_lower == 0 or key_num == 0 or len(password) != 8:
        return False

    return True


new_pass = '!q2w3e4R66'

print(len(new_pass))

result = is_valid_password(new_pass)
print(result)
