class PersonParent:
    def __init__(personParent, firstname, lastname, age):
        personParent.firstname = firstname
        personParent.lastname = lastname
        personParent.age = age

    def sayHello(personParent):
        return f"Hello from Parent"


class PersonChild(PersonParent):
    def __init__(personChild, firstname, lastname, age, salary):
        super().__init__(firstname, lastname, age)
        personChild.salary = salary

    def sayHello(personChild):
        return f"Hello from Child"



personParent = PersonParent("Ivan", "Ivcanov", 44,)
personChild = PersonChild("Ivan", "Ivcanov", 44, "Sofia")

print(personParent.sayHello())
print(personChild.sayHello())