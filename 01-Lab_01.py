"""
Exercise 1: Easy Level
Task:
Document a basic class using comments and docstrings.
 The class represents a simple Circle object with attributes 
 for radius and methods for calculating the area and 
 circumference.

 
 Task:
Add appropriate comments where necessary to explain the code
 logic.
Ensure that docstrings for the class, methods, and the 
constructor  (__init__) follow the same format.
"""

#code
import math

class Circle:
    

    def __init__(self, radius):

        self.radius = radius

    def area(self):

        return math.pi * self.radius ** 2

    def circumference(self):

        return 2 * math.pi * self.radius

# Example of creating a circle and getting its area and circumference
circle = Circle(5)
print(f"Area: {circle.area()}")
print(f"Circumference: {circle.circumference()}")
