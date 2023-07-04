class A:
    def __init__(self, value) -> None:
        self.value = value


class B(A):
    def __init__(self, name, age) -> None:
        super().__init__(name)
        self.age = age


b_class = B("Bill", 10)

print(b_class.value)
