"""
### Constructor: When Parent class has, but the child class has not
- **Short Explanation:** If a child class does not have its own constructor, it automatically uses the parent's constructor.
- **Practice Problem:** Create a base class `Person` with a constructor, and a child class `Employee` without a constructor.
- **Test Case Output:** 
  - `Employee inherits Person constructor`
"""
# Constructor: When Parent class has, but the child class has not
class Person:
    def __init__(self):
        print("Person constructor called")

class Employee(Person):
    pass

e = Employee()
