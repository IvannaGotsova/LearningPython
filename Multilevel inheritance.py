class Animal:

    def hello_animal(self):
        print("Hello from Animal")

class Mammal(Animal):

    def hello_mammal(self):
        print("Hello from Mammal")


class Cat(Mammal):

    def hello_cat(self):
        print("Hello from Cat")

class Dog(Mammal):

    def hello_dog(self):
        print("Hello from Dog")


animal = Animal()
animal.hello_animal()

mammal = Mammal()
mammal.hello_animal()
mammal.hello_mammal()

cat = Cat()
cat.hello_animal()
cat.hello_mammal()
cat.hello_cat()

dog = Dog()
dog.hello_animal()
dog.hello_mammal()
dog.hello_dog()