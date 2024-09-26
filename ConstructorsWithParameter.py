"""
### Constructors With Parameter
- **Short Explanation:** A constructor with parameters allows you to initialize an object with specific values.
- **Practice Problem:** Create a class `Employee` that takes name and salary as parameters in the constructor.
- **Test Case Output:** 
  - `Employee: Alice, Salary: 4000`
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

employee = Employee("Alice", 4000)
employee.display()