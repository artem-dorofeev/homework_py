class MyClass:
    def __init__(self, value):
        self.value = value

    def upper_val(self):
        return self.value.upper()

    def set_upper_value(self):
        self.value = self.upper_val()

    @staticmethod
    def get_general_info():
        return "General"


my_class = MyClass("New Value")


print(my_class.value)
print(MyClass.get_general_info())
# user_input = input(">>>>")

# user_class = MyClass(user_input)

# print(user_class.upper_val())
