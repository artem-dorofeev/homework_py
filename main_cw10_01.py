class MyClass:
    value = "New Value"


my_class = MyClass()
my_class1 = MyClass()

print(my_class.value)

MyClass.value = "Other"

my_class1.value = "hz"

print(my_class.value, my_class1.value)
