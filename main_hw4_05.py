def lookup_key(data, value):
    key_list = ['']
    for l, val in data.items():
        if value == val:
            print(l)
            key_list.append(l)

    key_list.remove('')
    return key_list


grade = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}
result = lookup_key(grade, 4)
print(result)
