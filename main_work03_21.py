# list = [0, 1]

# i = 1

# while i < 5:
#     list.append(i)
#     i += 1

# print(list)

# list_fibonacci = [0, 1]

# print(list_fibonacci)

# i = 1

# while i < 10:
#     list_fibonacci.append(list_fibonacci[i] + list_fibonacci[i-1])
#     i += 1

# print(list_fibonacci)

# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)


# def fibonacci(n):
#     global list_fibonacci
#     list_fibonacci.append(list_fibonacci[n] + list_fibonacci[n-1])


# fibonacci(5)
# print(list_fibonacci)

# result = list_fibonacci[2] + list_fibonacci[3]
# print(result)

# l_fib = [0, 1]


# def list_fib(n):

#     def fibonacci(n):
#         if n in (1, 2):
#             return n
#         else:
#             return fibonacci(n-1) + fibonacci(n-2)

#     global l_fib
#     i = 1
#     while i < n + 1:
#         l_fib.append(fibonacci(i))
#         i += 1
#     print(list_fib)


# result = list_fib(5)
# print(result)

def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fib_inp = int(input('>>>'))

result = fibonacci(fib_inp)
print(result)

# l_fib = [0, 1]
