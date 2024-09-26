"""
### Multilevel Inheritance
- **Short Explanation:** In multilevel inheritance, a class is derived from a class which is also derived from another class.
- **Practice Problem:** Create a class `Person`, a class `Employee` that inherits from `Person`, 
and a class `Manager` that inherits from `Employee`.
- **Test Case Output:** 
  - `Manager is a Person`
"""

# Multilevel Inheritance
class Person:
    def __init__(self):
        print("Person created")

class Employee(Person):
    def __init__(self):
        super().__init__()
        print("Employee created")

class Manager(Employee):
    def __init__(self):
        super().__init__()
        print("Manager is a Person")

m = Manager()
