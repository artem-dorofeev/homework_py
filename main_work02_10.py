while True:

    try:
        user_input = int(input('>>>'))
        print(user_input)
        break
    except ValueError as e:
        print(f"Not a number, {e}. Try again")

        
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
