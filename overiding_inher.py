# overiding in inheritance

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_area(self):
        return self.x * self.y


class Rectangle(Shape):
    def calculate_area(self):
        return self.x * self.y


area = Rectangle(4, 5)
print(area.calculate_area())
