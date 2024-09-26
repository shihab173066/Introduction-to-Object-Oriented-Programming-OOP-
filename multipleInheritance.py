"""
### Multiple Inheritance
- **Short Explanation:** Multiple inheritance occurs when a class inherits from more than one base class.
- **Practice Problem:** Create two classes `Teacher` and `Student`, and create a `TeachingAssistant` class that inherits from both.
- **Test Case Output:** 
  - `TeachingAssistant has both teacher and student roles`

"""
# Multiple Inheritance
class Teacher:
    def teach(self):
        return "Teaching"

class Student:
    def study(self):
        return "Studying"

class TeachingAssistant(Teacher, Student):
    def role(self):
        return "TeachingAssistant has both teacher and student roles"

ta = TeachingAssistant()
print(ta.role())
