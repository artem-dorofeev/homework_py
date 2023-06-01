grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    global grades
    result = []
    ch = 1

    for key, value in students.items():
        if value in grades:
            result.append('{:>4}|{:<10}|{:^5}|{:^5}'.format(
                ch, key, value, grades[value]))
            ch += 1

    return result


students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
result = formatted_grades(students)
print(result)


# for key, value in numbers.items():
#     print(key, value)

# def get_grade(key):
#     grade = {'F': 1, 'FX': 2, 'E': 3, 'D': 3, 'C': 4, 'B': 5, 'A': 5}
#     if key in grade:
#         return grade[key]
#     else:
#         return None


# def get_description(key):
#     grade = {'F': 'Unsatisfactorily', 'FX': 'Unsatisfactorily', 'E': 'Enough',
#              'D': 'Satisfactorily', 'C': 'Good', 'B': 'Very good', 'A': 'Perfectly'}
#     if key in grade:
#         return grade[key]
#     else:
#         return None
