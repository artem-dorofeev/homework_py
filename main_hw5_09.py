def formatted_numbers():
    result = ['|{:^10}|{:^10}|{:^10}|'.format("decimal", "hex", "binary")]
    str_result = ''

    for num in range(16):
        str_result = '|{n:<10d}|{n:^10x}|{n:>10b}|'.format(n=num)
        result.append(str_result)

    return result


for el in formatted_numbers():
    print(el)
