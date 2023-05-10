# result = None
# operand = None
# operator = None
# wait_for_number = True

# while True:


# a = None
# b = 10
# result = None
# while a == None:
#     b = input("input operand ")
# operator = input(">>>")
# if operator == '+':
#     result = a + b
# elif operator == '-':
#     result = a - b
# elif operator == '*':
#     result = a * b
# elif operator == '/':
#     result = a / b
# else:
#     print("unknow operator")
# print(result)


# x = None
# while x == None:
#     x = input(">>>")
#     if

# x = int(input(">>>"))
# if ord(x) >= 30 and ord(x) <=39:
# print(ord(x))
# c = int(x)
# print(x)

# while True:

#     try:
#         user_input = int(input('>>>'))
#         print(user_input)
#         break
#     except ValueError as e:
#         print(f"Not a number, {e}. Try again")
# print("work")
# x = str(user_input)
# print(x)


n1 = None
a = None
wait_for_number = False
n = None
result = None
result_text = str()
operators_str = "-+*/"


while True:

    try:
        n1 = int(input('Input operand: '))
        result = n1
        result_text += str(n1)
        print(result_text)
        break
    except ValueError as e:
        print(f"Not a number, {e}. Try again")


while True:
    if wait_for_number == False:
        a = input("Input operetor: ")
        if a == '=':
            break
        elif a in operators_str:
            result_text += a
            print(result_text)
            wait_for_number = True
        else:
            print("unknow operator")
    else:
        try:
            n = int(input("Input operand: "))
            result_text += str(n)
            print(result_text)
            wait_for_number = False
            if a == '+':
                result += n
            elif a == '-':
                result -= n
            elif a == '*':
                result *= n
            else:
                result /= n
        except ValueError as e:
            print(f"Not a number, {e}. Try again")

print(f'{result_text} = {result}')
