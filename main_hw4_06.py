def split_list(grade):
    list_min = list()
    list_max = list()
    if len(grade) > 0:
        summ = 0
        i = 0
        while i < len(grade):
            summ += grade[i]
            i += 1
        average = int(summ / len(grade))
        print(average)

        i = 0
        while i < len(grade):
            if grade[i] <= average:
                list_min.append(grade[i])
            else:
                list_max.append(grade[i])
            i += 1

    result = (list_min, list_max)

    return result


list_score = list()


result = split_list(list_score)
print(result)
