first_names = ["Ivan", "Petar", "Dimitar", "Stoqn", "Philip", "Stephan"]
last_names = ["Ivanov", "Petrov", "Dimitrov", "Stoqnov", "Philipov", "Stephanov"]
ages = (44, 45, 44, 40, 41, 43)
cities = ("Sofia", "Sofia", "Plovdiv", "Sofia", "Varna", "Sofia")

zipExample = zip(first_names, last_names, ages, cities)

for i in zipExample:
    print(i)
