class Dog:
    def make_sound(self):
        return "woof"


class Cat:
    def make_sound(self):
        return "mhew"


class Bird:
    def make_sound(self):
        return "cho cho cho"


def let_them_speak(obj):
    return obj.make_sound()


dog_obj = Dog()
cat_obj = Cat()
bird_obj = Bird()

print(let_them_speak(dog_obj))
print(let_them_speak(cat_obj))
print(let_them_speak(bird_obj))
