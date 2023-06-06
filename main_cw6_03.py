with open("class.txt") as file:
    while True:
        symbol = file.read(1)
        if not symbol:
            break
        print(symbol)


with open("class.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line)
