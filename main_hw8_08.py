from collections import Counter


def get_count_visits_from_ip(ips):
    ip_count = Counter(ips)
    result = {}
    for key, val in ip_count.items():
        result[key] = val
    return result


def get_frequent_visit_from_ip(ips):
    ip_count = Counter(ips)
    max = 0
    result = []
    for key, val in ip_count.items():
        if val > max:
            max = val
            result = (key, val)
    return result


IP = [
    "85.157.172.253", "10.99.1.1", "10.99.9.3", "10.99.9.3", "10.99.9.3",
    "10.99.1.1", "10.99.1.1", "10.99.9.3", "10.99.9.3", "10.99.9.3",
    "10.99.9.3", "10.99.1.1", "10.99.9.3", "10.99.9.3", "10.99.9.3",
    "10.99.1.1"]


result = get_count_visits_from_ip(IP)
result2 = get_frequent_visit_from_ip(IP)

print(result2)
print(result)

# for i in result2:
#     print(i)
"""
Є список IP адрес:

IP = [
    "85.157.172.253",
    ...
]
Реалізуйте дві функції. Перша get_count_visits_from_ip за допомогою Counter повертатиме словник, де ключ це IP, а значення – кількість входжень у вказаний список.
Приклад:

{
    '85.157.172.253': 2,
    ...
}

Друга функція get_frequent_visit_from_ip повертає кортеж з найбільш часто уживаним в списку IP і кількістю його появ в списку.

Пример:

('66.50.38.43', 4)

"""
