class PersonParent:
    def __init__(personParent, firstname, lastname, age):
        personParent.firstname = firstname
        personParent.lastname = lastname
        personParent.age = age

    def __str__(personParent):
        return f"{personParent.firstname} {personParent.lastname},  {personParent.age} years old."


class PersonChild(PersonParent):
    def __init__(personChild, firstname, lastname, age, salary):
        super().__init__(firstname, lastname, age)
        personChild.salary = salary


personChild = PersonChild("Ivan", "Ivanov", 44, 1000)

print(personChild.firstname)
print(personChild.lastname)
print(personChild.age)
print(personChild.salary)

print(personChild)