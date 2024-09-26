"""
### Constructor at Inheritance
- **Short Explanation:** Child classes can inherit the constructor of the parent class and extend or override its functionality.
- **Practice Problem:** Create a base class `Person` with a constructor, and a child class `Employee` that calls the parent's constructor.
- **Test Case Output:** 
  - `Person constructor called`
"""
# Constructor at Inheritance
class Person:
    def __init__(self):
        print("Person constructor called")

class Employee(Person):
    def __init__(self):
        super().__init__()
        print("Employee constructor called")

e = Employee()
