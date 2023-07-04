class A:
    name = "A"


class B(A):
    pass


b_class = B()

print(b_class.name)
