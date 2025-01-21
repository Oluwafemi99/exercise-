class Book:
    total_book = 0

    def __init__(self, name):
        self.name = name
        Book.total_book += 1

    @classmethod
    def display_total_book(cls):
        print(f"Total number of book created is: {cls.total_book}")


book1 = Book("Acts")
book2 = Book("John")
book3 = Book("Mark")

Book.display_total_book()
