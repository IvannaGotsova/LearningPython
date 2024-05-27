numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def filter_every_third(number):
    if number % 3 == 0:
        return True
    else:
        return False


print_list = filter(filter_every_third, numbers)

for i in print_list:
    print(i)