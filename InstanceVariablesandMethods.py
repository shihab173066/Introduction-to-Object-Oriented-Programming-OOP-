"""
### Instance Variables and Methods
- **Short Explanation:** Instance variables are tied to a specific object, and instance methods operate on them.
- **Practice Problem:** Create a class `Dog` with instance variables `name` and `breed` and a method `bark()`.
- **Test Case Output:** 
  - `Dog Name: Rex, Breed: Bulldog`
"""

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def display(self):
        print(f"Dog Name: {self.name}, Breed: {self.breed}")

dog = Dog("Rex", "Bulldog")
dog.display()
dog.bark()