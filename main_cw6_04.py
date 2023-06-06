with open("class.txt") as file:
    while True:
        chunk = file.read(1)
        if not chunk:
            break
        print(file.tell(), chunk)
