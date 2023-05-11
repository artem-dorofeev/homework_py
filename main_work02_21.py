# lst = [1, 2, 3, 6, 9, 10]
# print(max(lst))

# k = 0

# for i in lst:
#     if k < i:
#         k = i

# print(k)

a = 0
while a < 6:
    a += 1
    if not a % 2:
        continue
    print(a)
