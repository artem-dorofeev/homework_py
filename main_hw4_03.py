def format_ingredients(items):
    new_items = str(items[0])

    if len(items) > 1:
        i = 1
        while i < len(items):
            if i == len(items) - 1:
                new_items += ' and ' + str(items[i])
            else:
                new_items += ', ' + str(items[i])
            i += 1

    return new_items


pay_list = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]

print(pay_list)


new_list = format_ingredients(pay_list)
print(type(new_list))
print(new_list)
