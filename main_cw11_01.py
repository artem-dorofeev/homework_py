class Phone:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value

class User:
    def __init__(self, name, age = 22, phone=None) -> None:
        self.name = name
        self.age = age
        self.phone = phone

    def __str__(self) -> str:
        return f"User {self.name}, age {self.age}{', phone ' + str(self.phone) if self.phone else ''}"
        # return self.name


user = User("Bill")
user2 = User("Jimm", phone=Phone('+124124'))
print(user.name, user2.name)

print(user, user2)
