def get_favorites(contacts):
    result = []
    for i in filter(lambda x: x['favorite'], contacts):
        result.append(i)

    return result


name = [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}, {
    "name": "Vasa",
    "email": "11111111@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": True,
}, {
    "name": "Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "1111111111",
    "favorite": True,
}
]
result = get_favorites(name)
print(result)

"""
Завдання: відфільтрувати користувачів

Є список contacts, елементи якого - словники контактів наступного виду:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

Словник містить ім'я користувача, його email, телефонний номер та властивість - обраний контакт чи ні.

Створіть функцію get_favorites(contacts), яка повертатиме список, який містить лише обрані контакти. 
Використовуйте при цьому функцію filter, щоб відфільтрувати по полю favorite лише обрані контакти.


"""
