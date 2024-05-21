class Person:
    firstname = "Ivan"
    lastname = "Ivanov"
    age = 44

person = Person()

print(person.firstname)
print(person.lastname)
print(person.age)

class PersonOne:
    def __init__(personOne, firstname, lastname, age):
        personOne.firstname = firstname
        personOne.lastname = lastname
        personOne.age = age

    def __str__(personOne):
        return f"{personOne.firstname} {personOne.lastname},  {personOne.age} years old."

personOne = PersonOne("Petar", "Petrov", 44)

print(personOne.firstname)
print(personOne.lastname)
print(personOne.age)
print(personOne)

