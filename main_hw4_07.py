points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    global points

    if len(coordinates) <= 1 or coordinates == ['']:
        return 0

    distanse = 0

    i = 0
    while i < len(coordinates) - 1:
        start_point = coordinates[i]
        next_point = coordinates[i + 1]
        if next_point > start_point:
            finish_point = (start_point, next_point)
        else:
            finish_point = (next_point, start_point)
        distanse += points[finish_point]
        i += 1

    return distanse


point = [0, 1, 3, 2, 0]
print(point)

result = calculate_distance(point)
print(result)

# второй вариант поиска по координатам - от студента
# for i in range(len(coordinates) - 1):
#         point1 = coordinates[i]
#         point2 = coordinates[i + 1]
#         if (point1, point2) in points:
#             distance = points[(point1, point2)]
#         elif (point2, point1) in points:
#             distance = points[(point2, point1)]
#         else:
#             distance = 0
