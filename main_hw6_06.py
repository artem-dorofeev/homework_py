def get_recipe(path, search_id):
    result = {}
    with open(path, "r") as file:
        while True:
            line = file.readline()
            if not line:
                result = None
                break
            resept_list = line.rstrip().split(',')
            if search_id == resept_list[0]:
                result = {
                    "id": resept_list.pop(0),
                    "name": resept_list.pop(0),
                    "ingredients": resept_list
                }
                break
    return result

#             cats = {
#                 "id": list_cats[0],
#                 "name": list_cats[1],
#                 "age": int(list_cats[2])
#             }
#             result.append(cats)

#     return result


path = 'hw6_06.txt'
search_id = '60b90c3b13067a15887e1ae4'
# get_recipe(path, search_id)
result = get_recipe(path, search_id)
print(result)


"""
Кожен рецепт записаний з нового рядка (не забуваємо під час вирішення завдання про кінець рядка). Кожен запис починається з первинного ключа бази даних MongoDB. Далі через кому, йде назва рецепта, а потім через кому, йде перелік інгредієнтів рецепта.

Вам необхідно реалізувати функцію, котра буде отримувати інформацію про рецепт у вигляді словника для кожної страви що шукається. Створіть функцію get_recipe(path, search_id), яка повертатиме словник для рецепта із зазначеним ідентифікатором MongoDB.

Де параметри функції:

    path — шлях до файлу.
    search_id — первинний ключ MongoDB для пошуку рецепта

Вимоги:

    Використовуйте менеджер контексту with для читання з файлу
    Якщо рецепта із зазначеним search_id у файлі немає, функція повинна повернути None

Приклад: для файлу, вказаного вище, виклик функції у вигляді

get_recipe("./data/ingredients.csv", "60b90c3b13067a15887e1ae4")

Повинен знайти у файлі рядок 60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese і повернути результат у вигляді словника такої структури:

{
    "id": "60b90c3b13067a15887e1ae4",
    "name": "Watermelon Cucumber Salad",
    "ingredients": [
        "1 large seedless watermelon",
        "12 leaves fresh mint",
        "1 cup crumbled feta cheese",
    ],
}

"""
