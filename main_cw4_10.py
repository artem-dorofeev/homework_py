lst_m = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

# print(lst_m[2][1])

for lst in lst_m:
    for element in lst:
        print(element)

print(lst_m[1].pop(0))

print(lst_m)


def flatten(lst):
    if not lst:
        return []
    for i in lst:
        if isinstance(lst, list):
            return flatten(i)
        print(i)


flatten(lst_m)
