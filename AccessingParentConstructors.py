"""
### Accessing the Parent's Constructor
- **Short Explanation:** Use `super()` in the child class to access the parent's constructor.
- **Practice Problem:** Create a class `Person` and a class `Employee`, and use `super()` in the `Employee` class constructor.
- **Test Case Output:** 
  - `Parent constructor called`

"""
# Accessing the Parent's Constructor
class Person:
    def __init__(self):
        print("Parent constructor called")

class Employee(Person):
    def __init__(self):
        super().__init__()
        print("Employee constructor called")

e = Employee()
