# inheritance

class Animals:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"


class Dog(Animals):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print("woof")


dog = Dog("buddy")
print(dog.sleep())
print(dog.eat())
dog.bark()
