numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def add_one(number):
    return int(number) + 1


map_list = map(add_one, numbers)

print(list(map_list))
