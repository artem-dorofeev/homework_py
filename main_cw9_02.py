def pretty_func(value):
    def inner_funk(param):
        def inner_inner(param2):
            return value + param + param2
        return inner_inner
    return inner_funk


pretty_ten = pretty_func(10)
pretty_5 = pretty_func(5)

print(pretty_ten(1), pretty_5(1))
