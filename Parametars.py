def names (**names):
    for key, value in names.items():
        print("Hello " + value)

def add (*numbers):
    sum = 0
    numbers = list(numbers)
    numbers[0] = 100
    for x in numbers:
        sum += x
    print(sum)

names (first="Ivan", second="Petar", third="Dimitar", fourth="Stoqn", fifth="Philip", sixth="Stephan")
add (3, 4, 5)
