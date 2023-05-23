"""Dict"""

dct1 = {str(x): x**2 for x in range(10)}

for i in dct1:
    print(dct1[i])


for key in dct1.keys():
    print(key)


for value in dct1.values():
    print(value)

for key, value in dct1.items():
    print(f'{key} :   {value}')
