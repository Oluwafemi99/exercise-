class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multipy(x, y):
        return x * y


math1 = Calculator.add(5, 4)
math2 = Calculator.multipy(5, 4)
print(math1, math2)
