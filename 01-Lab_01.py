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
    """
    A class used to represet a circle.

    Attributes
    ----------
    radius : float
        The radius of the circle.

    Methods
    -------
    area():
        Calculates and returns the area of the circle.
    circumference():
        Calculates and returns the circumference of the circle.
    
    """
    
    def __init__(self, radius):
        """
        Initialize the circle with a specified radius.

        Parameters
        ----------
        radius : float
            The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the circumference of the circle.

        Returns
        -------
        float
            The circumference of the circle, calculated as 2 * pi * radius.
        """
        return math.pi * self.radius ** 2

    def circumference(self):

        return 2 * math.pi * self.radius

# Example of creating a circle and getting its area and circumference
circle = Circle(5) # Create a circle object with the radius 5
print(f"Area: {circle.area()}")  # Output the area of the circle
print(f"Circumference: {circle.circumference()}")  # Output the circumference of the circle