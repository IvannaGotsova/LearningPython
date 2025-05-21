class Example:

    def one(self):
        print("First method")
        return self

    def two(self):
        print("Second method")
        return self

    def three(self):
        print("Third method")
        return self

    def four(self):
        print("Fourth method")
        return self

    def five(self):
        print("Fifth method")
        return self




example = Example()

example.one().two().three().four().five()