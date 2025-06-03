class Library:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = True

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Book ID:", self.book_id)
        print("Available:", "Yes" if self.available else "No")

    def borrow(self):
        if self.available:
            self.available = False
            return "Book borrowed"
        else:
            return "Not available"

    def return_book(self):
        if not self.available:
            self.available = True
            return "Book returned"
        else:
            return "Already in library"

# Creating books
b1 = Library("Python", "Guido", 101)
b2 = Library("AI", "McCarthy", 102)

# Showing book details
b1.display()
print(b1.borrow())
print(b1.borrow())
print(b1.return_book())
print(b1.return_book())

