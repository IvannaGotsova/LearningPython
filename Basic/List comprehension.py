numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = [x for x in numbers if x % 2 != 0]
even_numbers = [x for x in numbers if x % 2 == 0]
name_numbers = ["odd" if x % 2 == 0 else "even "for x in numbers]

print(odd_numbers)
print(even_numbers)
print(name_numbers)


