lorem = "text ne pro chto ne o chem"

# print(lorem.upper())

lorem = lorem.upper()

find_l_fist = lorem.find('e'.upper())
find_l_last = lorem.rfind('e'.upper())

print(lorem[find_l_fist:find_l_last + 1])

# print(find_l)
