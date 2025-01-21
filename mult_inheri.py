# multiple Inheritance

class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying...")


class Mammal:
    def run(self):
        print(f"{self.name} is running...")


class Bat(Bird, Mammal):
    pass


bat = Bat("lee")
bat.fly()
bat.run()
