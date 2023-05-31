def is_check_name(fullname, first_name):
    fullname = fullname.lower()
    return fullname.startswith(first_name.lower())


full = 'Dorofeev Artem'
fist = 'dorofeev'

print(is_check_name(full, fist))
