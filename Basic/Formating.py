firstname = "Ivan"
lastName = "Ivanov"
age = 44
city = "Sofia"
salary = 1000

textToFormat = f"{firstname} {lastName}, {age} years old, from {city} - {salary:.2f}"
print(textToFormat)

textToFormat = "{0} {1}, {2} years old, from {3} - {4:.2f}"
print(textToFormat.format(firstname, lastName, age, city, salary))