def greeting(name, age):
    name_upper = name.upper()
    birth_year = 2023 - age
    return name_upper, birth_year


result = greeting('Bill', 12)
name, age = greeting('Bill', 12)

# print(type(greeting('Bill', 12)))

print(result[1])
print(age, name)
