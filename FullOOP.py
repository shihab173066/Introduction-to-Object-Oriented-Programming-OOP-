"""

### Static Properties in Inheritance Situations
- **Short Explanation:** Static properties are shared across instances and can be accessed without instantiating the class.
- **Practice Problem:** Create a base class with a static method, and call it from a derived class without instantiating either.
- **Test Case Output:** 
  - `Static method called`

---

### If Parent has static properties, child can access as it is like parent
- **Short Explanation:** The child class can access static properties of the parent class as if they belong to the child.
- **Practice Problem:** Create a static method in the parent class, and access it through the child class.
- **Test Case Output:** 
  - `Child class accessing Parent static method`

---

### If Child has static properties, Parent can't access as it is like child
- **Short Explanation:** Parent classes cannot access static properties of child classes directly.
- **Practice Problem:** Create a static property in the child class, and show that the parent class cannot access it.
- **Test Case Output:** 
  - `Parent cannot access child static property`

---

### How Child can access Parent's static and non-static properties
- **Short Explanation:** The child class can access the parent's static properties using `ClassName.property` and non-static properties through inheritance.
- **Practice Problem:** Create a parent class with static and non-static properties, and access them in the child class.
- **Test Case Output:** 
  - `Child accessing Parent's properties`

---

### Method Overriding
- **Short Explanation:** Method overriding allows a child class to provide a specific implementation of a method already defined in the parent class.
- **Practice Problem:** Create a `Parent` class with a `speak()` method, and override it in the `Child` class.
- **Test Case Output:** 
  - `Child's speak method`

---

### Method Overloading
- **Short Explanation:** Method overloading allows multiple methods with the same name but different parameters.
- **Practice Problem:** Create a class with overloaded `add()` methods that work with both two and three parameters.
- **Test Case Output:** 
  - `Addition result: 10 (with two params), 15 (with three params)`

---

### Method Overloading Using Default Arguments
- **Short Explanation:** Default arguments allow method overloading by providing default values for parameters.
- **Practice Problem:** Create a method `calculate()` that can work with one or two parameters by using default arguments.
- **Test Case Output:** 
  - `Calculated value with one argument: 10`
  - `Calculated value with two arguments: 20`

---

### Method Overloading Using Variable-Length Arguments
- **Short Explanation:** Variable-length arguments allow a method to accept an arbitrary number of parameters.
- **Practice Problem:** Create a method `add()` that can take multiple parameters using `*args`.
- **Test Case Output:** 
  - `Sum of numbers: 30`

---

### Abstract Class in Python
- **Short Explanation:** An abstract class is a blueprint for other classes and cannot be instantiated. It contains abstract methods that must be implemented in child classes.
- **Practice Problem:** Create an abstract class `Shape` with an abstract method `area()`, and implement it in derived classes like `Circle` and `Square`.
- **Test Case Output:** 
  - `Area of circle: 50.27`

---

### Key Points of Abstract Classes
1. Cannot be instantiated directly.
2. Must have at least one abstract method.
3. Forces subclasses to provide implementations for abstract methods.
4. Allows the use of `@abstractmethod` decorator from the `abc` module.

**Practice Problem:**  
Create an abstract class `Vehicle` with an abstract method `drive()`. Create subclasses `Car` and `Bike` that implement `drive()` method uniquely.

**Test Case:**  
Input: `Car: "Driving a car", Bike: "Riding a bike"`  
Output: `Car: Driving a car, Bike: Riding a bike`

---

### Access Modifiers
Access modifiers control how class variables or methods can be accessed. Python uses conventions for access control.

---

### Public (No leading underscore)
A **public** member (variables or methods) is accessible from anywhere inside or outside the class. No leading underscore is used for public members.

**Practice Problem:**  
Create a class `Employee` with a public attribute `name`. Set the `name` publicly and print it.

**Test Case:**  
Input: `name = "John"`  
Output: `John`

---

### Protected (Single leading underscore: `_`)
A **protected** member is indicated by a single leading underscore (`_`) and is meant to be used within the class and its subclasses, but not meant to be accessed directly from outside.

**Practice Problem:**  
Create a class `Employee` with a protected attribute `_salary`. In a subclass, modify the `_salary` and access it within the class.

**Test Case:**  
Input: `_salary = 5000`  
Output: `Modified salary: 7000`

---

### Private (Double leading underscore: `__`)
A **private** member is indicated by a double leading underscore (`__`). It is only accessible within the class where it is defined, and it undergoes name mangling to prevent external access.

**Practice Problem:**  
Create a class `BankAccount` with a private attribute `__balance`. Try to access and modify it both directly and via a public method.

**Test Case:**  
Input: `__balance = 10000, deposit 2000 via public method`  
Output: `Access denied, balance after deposit: 12000`

---

### Getter Setter
**Getter and Setter** methods are used to control access to class attributes, ensuring proper validation and encapsulation.

**Practice Problem:**  
Create a class `Student` with a private attribute `__grade`. Use getter and setter methods to access and modify the grade with validation (e.g., grades must be between 0 and 100).

**Test Case:**  
Input: `Set grade = 85, Set invalid grade = 110`  
Output: `Valid grade: 85, Error: Invalid grade`

---

### Encapsulation
**Encapsulation** is the concept of bundling data (attributes) and methods that operate on the data into a single unit or class. It restricts direct access to some of the object's components, which can help protect the integrity of the data.

**Practice Problem:**  
Create a class `Person` with private attributes `__name` and `__age`. Use getter and setter methods to modify these attributes and prevent invalid age values.

**Test Case:**  
Input: `Set name: "Alice", Set age: 25, Set invalid age: -5`  
Output: `Name: Alice, Age: 25, Error: Invalid age`

---

### Polymorphism
**Polymorphism** allows different classes to implement the same method in different ways. It enables a common interface for different types of objects.

**Practice Problem:**  
Create a class `Animal` with a method `speak()`. Create subclasses `Dog` and `Cat` that implement `speak()` differently.

**Test Case:**  
Input: `Dog speaks, Cat speaks`  
Output: `Dog: Woof! Cat: Meow!`

---

### Key Points of Polymorphism
1. Polymorphism allows different classes to define the same method in their own way.
2. It enables method overloading and method overriding.
3. Supports code reusability and flexibility.

**Practice Problem:**  
Create a function that accepts objects of different types (e.g., `Dog`, `Cat`, and `Cow`) and calls their `speak()` method without checking their type.

**Test Case:**  
Input: `Dog speaks, Cat speaks, Cow speaks`  
Output: `Dog: Woof!, Cat: Meow!, Cow: Moo!`
"""

from abc import ABC, abstractmethod

### Static Properties in Inheritance Situations
class Base:
    @staticmethod
    def static_method():
        print("Static method called")

class Derived(Base):
    pass

# Call static method from the derived class without instantiating either
Derived.static_method()

### If Parent has static properties, child can access as it is like parent
class Parent:
    @staticmethod
    def parent_static_method():
        print("Child class accessing Parent static method")

class Child(Parent):
    pass

# Child can access parent's static method
Child.parent_static_method()

### If Child has static properties, Parent can't access as it is like child
class ChildWithStatic:
    @staticmethod
    def child_static_method():
        print("Parent cannot access child static property")

class ParentOfChildWithStatic:
    pass

# Parent can't access child's static method
try:
    ParentOfChildWithStatic.child_static_method()
except AttributeError:
    print("Parent cannot access child static property")

### How Child can access Parent's static and non-static properties
class ParentWithProperties:
    static_property = "Static Property"
    
    def __init__(self):
        self.non_static_property = "Non-static Property"

class ChildAccessingParentProperties(ParentWithProperties):
    def show_properties(self):
        print(f"Accessing Parent's static property: {ParentWithProperties.static_property}")
        print(f"Accessing Parent's non-static property: {self.non_static_property}")

# Child accessing both static and non-static properties of Parent
child_instance = ChildAccessingParentProperties()
child_instance.show_properties()

### Method Overriding
class ParentWithSpeak:
    def speak(self):
        print("Parent's speak method")

class ChildWithSpeak(ParentWithSpeak):
    def speak(self):
        print("Child's speak method")

# Child's method overriding Parent's method
child = ChildWithSpeak()
child.speak()

### Method Overloading (Using default arguments for Python)
class MathOperations:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        return a + b

# Overloading behavior with two and three arguments
math_ops = MathOperations()
print(f"Addition result with two params: {math_ops.add(3, 7)}")
print(f"Addition result with three params: {math_ops.add(3, 5, 7)}")

### Method Overloading Using Default Arguments
class Calculator:
    def calculate(self, x, y=10):
        return x + y

# Calculating with default and two arguments
calc = Calculator()
print(f"Calculated value with one argument: {calc.calculate(10)}")
print(f"Calculated value with two arguments: {calc.calculate(10, 10)}")

### Method Overloading Using Variable-Length Arguments
class Adder:
    def add(self, *args):
        return sum(args)

# Adding multiple numbers using *args
adder = Adder()
print(f"Sum of numbers: {adder.add(5, 10, 15)}")

### Abstract Class in Python
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * (self.radius ** 2)

# Derived class implementing abstract method
circle = Circle(4)
print(f"Area of circle: {circle.area()}")

### Abstract Class Key Points
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Driving a car")

class Bike(Vehicle):
    def drive(self):
        print("Riding a bike")

# Testing abstract classes
car = Car()
bike = Bike()
car.drive()
bike.drive()

### Access Modifiers
### Public (No leading underscore)
class Employee:
    def __init__(self, name):
        self.name = name  # Public attribute

# Accessing public attribute
employee = Employee("John")
print(employee.name)

### Protected (Single leading underscore)
class EmployeeProtected:
    def __init__(self, salary):
        self._salary = salary  # Protected attribute

    def modify_salary(self):
        self._salary += 2000
        print(f"Modified salary: {self._salary}")

# Accessing protected attribute within the class
employee_protected = EmployeeProtected(5000)
employee_protected.modify_salary()

### Private (Double leading underscore)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Balance after deposit: {self.__balance}")

# Accessing private attribute via a method
account = BankAccount(10000)
account.deposit(2000)

### Getter Setter
class Student:
    def __init__(self):
        self.__grade = None  # Private attribute

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Error: Invalid grade")

# Accessing and modifying private attribute using getter and setter
student = Student()
student.set_grade(85)
print(f"Valid grade: {student.get_grade()}")
student.set_grade(110)

### Encapsulation
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attributes
        self.__age = age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Error: Invalid age")

    def get_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

# Encapsulation with getter/setter
person = Person("Alice", 25)
person.get_info()
person.set_age(-5)

### Polymorphism
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Polymorphism allows treating objects of different types the same way
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
