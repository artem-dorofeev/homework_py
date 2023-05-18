import turtle

turtle.setup(1000, 1000)


def fibonacci(n):
    if n in (1, 2):
        return 1
    if not n:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)


t = turtle.Turtle()

for i in range(15):
    t.circle(fibonacci(i), 90)

# t.forward(100)

turtle.mainloop()
