# import builtins

# print(dir(builtins))

# file = open("d:\\")

with open("class.txt", "w") as file:
    for _ in range(10):
        file.write("Hello\n")
