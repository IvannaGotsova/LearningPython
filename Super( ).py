class Parent:
    def __init__(self, name):
        self.nameSelf = name

    def name(self):
        print(self.nameSelf)


class Child(Parent):
    def __init__(self, name):
        super().__init__(name)


childExample = Child("Ivan Ivanov")

childExample.name()
