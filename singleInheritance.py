"""
### Single Inheritance
- **Short Explanation:** In single inheritance, a class inherits from only one base class.
- **Practice Problem:** Create a class `Vehicle` and another class `Car` that inherits from `Vehicle`.
- **Test Case Output:** 
  - `Car is a type of Vehicle`
"""
class Vehicle:

    def show(self):
        return "Car is a type of vehicle"
    
class Car(Vehicle):
    pass

obj = Car()

print(obj.show())