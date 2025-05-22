class Animal:

    def hello_animal(self):
        print("Hello from Animal")

class Mammal():

    def hello_mammal(self):
        print("Hello from Mammal")


class Cat(Animal, Mammal):

    def hello_cat(self):
        print("Hello from Cat")

class Dog(Animal, Mammal):

    def hello_dog(self):
        print("Hello from Dog")


animal = Animal()
animal.hello_animal()

mammal = Mammal()
mammal.hello_mammal()

cat = Cat()
cat.hello_animal()
cat.hello_mammal()
cat.hello_cat()

dog = Dog()
dog.hello_animal()
dog.hello_mammal()
dog.hello_dog()