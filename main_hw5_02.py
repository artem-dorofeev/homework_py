articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    global articles_dict
    new_list = []
    lower_list = []
    lower_find = key.lower()

    for i in articles_dict:

        for value in i.values():

            if type(value) == str:
                if letter_case:
                    lower_list = value
                    lower_find = key
                else:
                    lower_list = value.lower()
                    lower_find = key.lower()

                if lower_list.find(lower_find) >= 0:
                    new_list.append(i)

    return new_list


print(find_articles("Ocean", True))

# find = "Ocean"
# lower_find = find.lower()

# print(new_list)
# print(find, lower_find)

# print(value.find("ocean"))

# if key.find("are") > 0 or value.find("are") > 0:
#     print("This OK!!")


# print(articles_dict[0])
