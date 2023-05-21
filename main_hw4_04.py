def get_grade(key):
    grade = {'F': 1, 'FX': 2, 'E': 3, 'D': 3, 'C': 4, 'B': 5, 'A': 5}
    if key in grade:
        return grade[key]
    else:
        return None


def get_description(key):
    grade = {'F': 'Unsatisfactorily', 'FX': 'Unsatisfactorily', 'E': 'Enough',
             'D': 'Satisfactorily', 'C': 'Good', 'B': 'Very good', 'A': 'Perfectly'}
    if key in grade:
        return grade[key]
    else:
        return None


result = get_grade('FX')
result2 = get_grade('t')
result3 = get_grade('A')
print(result)
print(result2)
print(result3)


result4 = get_description('FX')
result5 = get_description('t')
result6 = get_description('A')
print(result4)
print(result5)
print(result6)
