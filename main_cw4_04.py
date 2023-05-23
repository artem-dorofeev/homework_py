from string import ascii_letters

lst = [x for x in ascii_letters]

lst.insert(-1, "Hello")

print(lst)
