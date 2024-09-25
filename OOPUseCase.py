"""
### OOP Use Case
- **Short Explanation:** OOP is used in situations where we model real-world entities with properties and behaviors, 
like bank systems or inventory management.
- **Practice Problem:** Build a class for a library system with attributes for book name, author, and methods for borrowing and returning
 books.

- **Test Case Output:** 
  - `Book borrowed: Harry Potter by J.K. Rowling`
"""

class librarySystem:
    
    book_name = " "
    author = " "

    def borrowing(self, book_name, author):
        self.book_name = book_name
        self.author = author
        return (f"Borrowing Book: {self.book_name} by {self.author}")

    def returning(self):
        return (f"Returning Book: {self.book_name} by {self.author}")
    
reader = librarySystem()
print(reader.borrowing("Harry Potter", "J.K. Rowlin"))
print(reader.returning())
