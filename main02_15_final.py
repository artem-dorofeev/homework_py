result = None
operand = None
operand1 = None
operator = None
wait_for_number = False
result_text = str()
operators_str = "-+*/"

while True:

    try:
        operand1 = int(input('Input operand: '))
        result = operand1
        result_text += str(operand1)
        break
    except ValueError as e:
        print(f"Not a number, {e}. Try again")


while True:
    if wait_for_number == False:
        operator = input("Input operetor: ")
        if operator == '=':
            break
        elif operator in operators_str:
            result_text += operator
            wait_for_number = True
        else:
            print("unknow operator")
    else:
        try:
            operand = int(input("Input operand: "))
            result_text += str(operand)
            wait_for_number = False
            if operator == '+':
                result += operand
            elif operator == '-':
                result -= operand
            elif operator == '*':
                result *= operand
            else:
                result /= operand
        except ValueError as e:
            print(f"Not a number, {e}. Try again")

print(f'{result_text} = {result}')
