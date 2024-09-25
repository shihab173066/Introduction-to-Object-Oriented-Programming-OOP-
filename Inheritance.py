"""
### Inheritance
- **Short Explanation:** Inheritance allows a class to inherit attributes and methods from another class.
- **Practice Problem:** Create a base class `Animal` and a derived class `Dog` that inherits from `Animal`.
- **Test Case Output:** 
  - `Animal: 
     Dog`
"""
class Animal:

    def show(self):
        print("Animal:")

class Dog(Animal):


    def showDog(self):
        print("Dog")


obj = Dog()
obj.show()
obj.showDog()
