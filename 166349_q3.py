class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed.")

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has no borrowed books.")

# Sample interactive system
def main():
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    member = LibraryMember("Alice", "M001")
    books = [book1, book2, book3]

    while True:
        choice = input("\n1. Borrow 2. Return 3. List 4. Exit\nChoose: ")
        if choice == "1":
            for i, book in enumerate(books):
                print(f"{i+1}. {book.title} - {'Available' if not book.is_borrowed else 'Not Available'}")
            idx = int(input("Enter book number to borrow: ")) - 1
            if 0 <= idx < len(books):
                member.borrow_book(books[idx])
        elif choice == "2":
            for i, book in enumerate(member.borrowed_books):
                print(f"{i+1}. {book.title}")
            idx = int(input("Enter book number to return: ")) - 1
            if 0 <= idx < len(member.borrowed_books):
                member.return_book(member.borrowed_books[idx])
        elif choice == "3":
            member.list_borrowed_books()
        elif choice == "4":
            print("Exiting system.")
            break

if __name__ == "__main__":
    main()
