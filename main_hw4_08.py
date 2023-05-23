def game(terra, power):
    energy = 1
    print(terra, power)
    for list in terra:
        print(list)
        for number in list:
            print(number)
            if power >= number:
                energy += number
                power = energy
            else:
                break

    return energy


user = [[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]]
# user = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
print(game(user, 1))
# user2 = [[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]]
# print(game(user2, 1))
