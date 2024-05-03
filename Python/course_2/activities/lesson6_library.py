from lesson6 import Book

book1 = Book('The Great Gatsby', 'F. Scott Fitzgerald', 1925)
book2 = Book('To kill a Mockingbird', 'Harper Lee', 1960)
Book.to_borrow(book1)
# print(book1)

input_year = input("Enter a year to check for available book: ")
Book.is_able(input_year)
