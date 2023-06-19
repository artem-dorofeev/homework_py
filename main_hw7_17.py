def encode(data):
    if not data:
        return []
    count = 1
    current = data[0]
    while count < len(data) and data[count] == current:
        count += 1

    return [current, count] + encode(data[count:])


test_list = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
test_list2 = [1, 2, 5, 7]
result = encode(test_list)
print(result)


"""
Повернемося до попереднього завдання та виконаємо зворотне. Напишіть рекурсивну функцію encode для кодування списку або рядка. 
Як аргумент функція приймає список ( наприклад ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]) 
або рядок (наприклад, "XXXZZXXYYYZZ"). Функція повинна повернути закодований список елементів (наприклад ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).

"""
