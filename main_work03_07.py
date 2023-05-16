def greeting(name, *numbers):
    text = ''
    for i in numbers:
        text += i + '\n'

    return f'{name}: {text}'


print(greeting('Bill', 'Bill', 'Bill', 'Bill', 'Bill', 'Bill'))
