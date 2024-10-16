import math

# Code Smell 1: Long method
def calculate_area_and_perimeter(shape, radius=0, length=0, width=0):
    if shape == 'circle':
        # Code Smell 2: Magic numbers
        area = math.pi * (radius ** 2)
        perimeter = 2 * math.pi * radius
    elif shape == 'square':
        # Code Smell 3: Duplicated code
        area = length * length
        perimeter = 4 * length
    elif shape == 'rectangle':
        area = length * width
        perimeter = 2 * (length + width)
    else:
        # Code Smell 4: No error handling
        print("Invalid shape")
        return

    # Code Smell 5: Global variable usage
    global last_area
    last_area = area

    # Code Smell 6: Print statements for debugging
    print(f"Area: {area}, Perimeter: {perimeter}")

    return area, perimeter

# Code Smell 7: Unused variables
unused_var = "I'm not used"

# Code Smell 8: Large class
class ShapeAnalyzer:
    def __init__(self, shape):
        self.shape = shape
    
    # Code Smell 9: Too many responsibilities
    def analyze(self, radius=0, length=0, width=0):
        result = calculate_area_and_perimeter(self.shape, radius, length, width)
        
        # Code Smell 10: Deep nesting
        if self.shape == 'circle':
            if radius > 0:
                if radius < 10:
                    print("Small circle")
                else:
                    print("Large circle")
            else:
                print("Invalid radius")
        return result
    
    # Code Smell 11: Misleading variable names
    def analyze_shape2(self):
        print("Analyzing shape 2...")

# Code Smell 12: Inconsistent naming
def perform_shape_check():
    sa = ShapeAnalyzer("circle")
    sa.analyze(radius=5)
    # Code Smell 13: Hard-coded strings
    return "Check completed"

# Code Smell 14: Unused imports
import os

# Code Smell 15: Lack of documentation
def bad_function():
    # Code Smell 16: Long parameter list
    print("This is a bad function")

# Code Smell 17: Mutable default arguments
def append_to_list(element, my_list=[]):
    my_list.append(element)
    return my_list

# Code Smell 18: Use of wildcard imports
from math import *

# Code Smell 19: Not closing file properly
def read_file(file_name):
    f = open(file_name, 'r')
    data = f.read()
    return data

# Code Smell 20: Overcomplicated conditionals
def check_value(value):
    if value > 10 and value % 2 == 0 and (value < 100 or value == 100) and value != 50:
        return True
    return False
