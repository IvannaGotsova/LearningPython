
personFour = {
    "firstName": "Stoqn",
    "lastName": "Stoqnov",
    "age": 47
}

dictionaryPeople = {
  "personOne" : {
    "firstName": "Ivan",
    "lastName": "Ivanov",
    "age": 44
  },
  "personTwo": {
    "firstName": "Petar",
    "lastName": "Petrov",
    "age": 45
  },
  "personThree": {
    "firstName": "Dimitar",
    "lastName": "Dimitrov",
    "age": 46
  },
  "personFour" : personFour
}

print(dictionaryPeople["personFour"]["firstName"])

for x in dictionaryPeople:
    print(x, dictionaryPeople[x])