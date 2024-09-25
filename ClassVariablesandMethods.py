"""
### Class Variables and Methods
- **Short Explanation:** Class variables are shared across all instances of the class, 
while instance variables are unique to each instance.
- **Practice Problem:** Create a class with a class variable counting the number of objects created.
- **Test Case Output:** 
  - `Total persons created: 2`
"""
class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

person1 = Person()
person2 = Person()
print("Total persons created:", Person.get_count())