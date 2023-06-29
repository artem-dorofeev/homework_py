def normal_name(list_name):
    result = []
    for i in map(lambda x: x.capitalize(), list_name):
        result.append(i)

    # for i in list_name:
    #     result.append(i.capitalize())

    return result


name = ["dan", "jane", "steve", "mike"]

result = normal_name(name)
print(result)

"""


Є список name з іменами користувачів, але всі починаються з малої літери.

name = ["dan", "jane", "steve", "mike"]

Розробіть функцію normal_name, яка приймає список імен та повертає теж список імен, але вже з правильними іменами з великої літери.

['Dan', 'Jane', 'Steve', 'Mike']

Необхідно використовувати функцію map. Не забудьте, що необхідно виконати перетворення типів для map.


"""
