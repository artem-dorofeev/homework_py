# список

lst = []
lst1 = list()

lst2 = [1, 2, 3, 4]
print(lst2)

for i in range(10):
    lst1.append(i)

print(lst1)


# print(lst[3])


for i in lst1:
    print(i)


for index, item in enumerate(lst1):
    print(index, item)
