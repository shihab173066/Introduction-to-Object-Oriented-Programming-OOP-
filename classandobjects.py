"""
### Creating Classes and Objects
- **Short Explanation:** Classes are blueprints for objects. Objects are instances of classes.
- **Practice Problem:** Create a class `Person` with name and age, and instantiate two objects with different attributes.
- **Test Case Output:** 
  - `Name: Alice, Age: 30`
"""

class Person:
    name = "Alice"
    age = 30

human = Person()
print(f"Name: {human.name}, Age: {human.age}")