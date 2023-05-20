def amount_payment(payment):
    sum = 0
    i = 0

    while i < len(payment):
        if payment[i] > 0:
            sum += payment[i]
        i += 1

    return sum


pay_list = [1, 10,  -8, -5, 25, -3]
print(amount_payment(pay_list))
