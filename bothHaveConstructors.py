"""
### Constructor: When Parent and child both have constructor
- **Short Explanation:** When both classes have constructors, the child class can call the parent's constructor using `super()`.
- **Practice Problem:** Create a `Parent` class with a constructor, 
and a `Child` class with its own constructor that calls the parent’s constructor.
- **Test Case Output:** 
  - `Child constructor called after Parent constructor`

"""
# Constructor: When Parent and child both have constructor
class Parent:
    def __init__(self):
        print("Parent constructor called")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor called after Parent constructor")

c = Child()
