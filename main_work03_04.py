greeting = 'hello'

print(globals())


def print_greeting():
    global greeting
    greeting = 'Aloha world'
    print(greeting)


print_greeting()
print(globals())
