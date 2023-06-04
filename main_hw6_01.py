# def total_salary(path):


fh = open('test.txt', 'w')
fh.write('hello!2')
fh.close()

text = ''

fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    text = text + symbol
    print(symbol)
print(text)
fh.close()
