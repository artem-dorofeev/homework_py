def get_grade(key):
    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade.get(key, None)


def get_description(key):
    description = {
        "A": "Perfectly",
        "B": "Very good",
        "C": "Good",
        "D": "Satisfactorily",
        "E": "Enough",
        "FX": "Unsatisfactorily",
        "F": "Unsatisfactorily",
    }
    return description.get(key, None)


def get_student_grade(option):
    if option == "grade":
        return get_grade
    elif option == "description":
        return get_description


"""
Реалізуйте функцію вищого порядку get_student_grade, яка приймає параметр option. 
Якщо він дорівнює значенням "grade", то функція повертає функцію get_grade, а якщо його значення дорівнює "description", 
то повертає функцію get_description. Якщо параметр за значенням не співпав із заданими, то функція get_student_grade повинна повертати значення None.

"""
