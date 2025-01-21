def calculate(x, y, operation):
    match operation:
        case "add":
            result = x+y
        case "subtract":
            result = x-y
        case "multiply":
            result = x*y
        case "divide":
            if y == 0:
                result = "error"
            else:
                result = x/y
        case _:
            "error"
    print(result)


"""
def main():
    x = int(input("enter a no: "))
    y = int(input("enter a no: "))
    operation = input("enter the operation(add, subtract, multipy, divide): ")
    calculate(x, y, operation)
"""

# main()
calculate(5, 2, operation="divide")
