def greeting(name: str, age: int) -> str:
    if age > 18:
        return f'Hello {name}'
    else:
        return 'No entrance'


result = greeting('Bill', 20)

print(result)
