"""
### Introduction to Object-Oriented Programming (OOP)
- **Short Explanation:** OOP is a programming paradigm based on the concept of "objects", which can contain data and methods.
- **Practice Problem:** Create a basic class for a car that has attributes like `make`, `model`, and `year` 
and methods to start and stop the car.

- **Test Case Output:** 
  - `Car make: Toyota, Model: Corolla, Year: 2022`
  - `Car started`
"""

class Car:
    Make = "Toyota"
    Model = "Corolla"
    Year = 2022

    def startCar(self):
        return ("Car Started")

    def stopCar(self):
        return ("Stop Car")

transport = Car()

print(transport.Make)
print(transport.Model)
print(transport.Year)
print(transport.startCar())
print(transport.stopCar())
    