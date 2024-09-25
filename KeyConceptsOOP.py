"""
### Key Concepts of OOP
- **Short Explanation:** The key OOP concepts include encapsulation, inheritance, abstraction, and polymorphism.
- **Practice Problem:** Demonstrate encapsulation by creating a class with private attributes and public getter and setter methods.
- **Test Case Output:** 
  - `Salary: 5000`
"""

class EmployeeSalary:

    __salary = 0

    def getter(self):
        return self.__salary
    
    def setter(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary!")

pay = EmployeeSalary()

print(pay.getter()) # inital balance will be returned 
pay.setter(80000) # balanace updated 
print(pay.getter()) # new balance will be returned 


