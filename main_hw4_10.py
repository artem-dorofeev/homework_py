from random import randint


def get_random_password():
    new_pass = ''

    for i in range(8):
        new_pass += chr(randint(40, 126))

    return new_pass


print(get_random_password())
print(get_random_password())
print(get_random_password())
