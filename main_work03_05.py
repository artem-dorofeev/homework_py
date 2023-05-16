def print_greeting():
    greeting = 'Aloha world'
    print(greeting)

    def local_greeting():
        nonlocal greeting
        # greeting = 'Hello from ZP'
        print(greeting)

    local_greeting()


print_greeting()
