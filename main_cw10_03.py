class MyClass:
    def __init__(self, value):
        self.value = value
        # pass

    def upper_val(self):
        return self.value.upper()

    def set_upper_value(self):
        self.value = self.upper_val()



my_pyryatyn = MyClass("New Value")

# my_class1 = MyClass()

# print(my_pyryatyn.value)

print(my_pyryatyn.upper_val())

user_input = input(">>>>")

user_class = MyClass(user_input)

print(user_class.upper_val())
