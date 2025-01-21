# calculator.py module
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "error"
    else:
        return x / y


def main():
    x = int(input("enter no"))
    y = int(input("enter no"))
    operator = input("add", "subtract", "multiply", "divide")


main()
