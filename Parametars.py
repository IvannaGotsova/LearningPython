def add (*numbers):
    sum = 0
    numbers = list(numbers)
    numbers[0] = 100
    for x in numbers:
        sum += x
    print(sum)


add(3, 4, 5)
