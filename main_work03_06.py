def greeting(name: str, age: int = 18) -> str:
    return f'{name}: {age}'


print(greeting(name='Bill'))
