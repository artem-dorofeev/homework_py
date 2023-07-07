from collections import UserString


class NumberString(UserString):
    def number_count(self):
        count = 0
        for i in self.data:
            if ord(i) >= 48 and ord(i) <= 57:
                count += 1
        return count


test_str = "ksgfj 7 kjs 888 shgjhsg 99 lslgn2"
result = NumberString(test_str)
print(result.number_count())
# test_str = NumberString('w1w1w222')
# result = test_str.number_count()
# print(result)

"""

Створіть клас NumberString, успадкуйте його від класу UserString, визначте для нього метод 
number_count(self), який буде рахувати кількість цифр у рядку.

"""
