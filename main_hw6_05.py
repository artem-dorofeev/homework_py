def get_cats_info(path):
    result = []
    with open(path, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            list_cats = line.strip().split(',')
            cats = {
                "id": list_cats[0],
                "name": list_cats[1],
                "age": int(list_cats[2])
            }
            result.append(cats)

    return result


path = 'hw6_05.txt'
result = get_cats_info(path)
print(result)


"""

Ми маємо таку структуру файлу:

60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5

Кожен запис складається з трьох частин і починається з нового рядка. Наприклад, для першого запису початок 60b90c1c13067a15887e1ae1 — це первинний ключ бази даних MongoDB. Він завжди містить 12 байтів або рівно 24 символи. Далі ми бачимо прізвисько кота Tayson та його вік 3. Всі частини запису розділені символом кома ,

Розробіть функцію get_cats_info(path), яка повертатиме список словників із даними котів у вигляді:

[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]

Параметри функції:

    path - шлях до файлу

Вимоги:

    прочитайте вміст файлу за допомогою режиму "r".
    ми використовуємо менеджер контексту with
    поверніть із функції список котів із файлу у потрібному форматі


"""
