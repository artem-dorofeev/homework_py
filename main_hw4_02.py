def prepare_data(data):
    min = max = data[0]
    i = 1
    while i < len(data):
        if min > data[i]:
            min = data[i]
        if max < data[i]:
            max = data[i]
        i += 1

    while min in data:
        data.remove(min)

    while max in data:
        data.remove(max)

    data.sort()

    return data


pay_list = [1, 10,  -8, -5, 25, -3, 35, 44, -2, 44, 44, -8, -8]
print(pay_list)
print(prepare_data(pay_list))
