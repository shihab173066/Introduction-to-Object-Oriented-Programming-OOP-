"""
### Constructors Without Parameter
- **Short Explanation:** A constructor is a special method used to initialize objects. Without parameters, it sets default values.
- **Practice Problem:** Create a class `Student` that sets a default name and age if none are provided.
- **Test Case Output:** 
  - `Default Name: John, Age: 18`
"""

class Student:
    def __init__(self):
        self.name = "John"
        self.age = 18

    def display(self):
        print(f"Default Name: {self.name}, Age: {self.age}")

student = Student()
student.display()