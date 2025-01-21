"""
rows = 5
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
"""

# Reuseable version of creating a pyramid

# creating pyramid function


def pyramid(rows):
    for i in range(rows):
        for k in range(rows - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()


# input for the pyramid function
def main():
    rows = int(input("Enter no of rows: "))
    pyramid(rows)


main()
pyramid(6)
pyramid(7)