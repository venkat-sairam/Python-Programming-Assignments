
'''
    1. Write a python program to Print Hello Python.
'''

print("1. A python program to Print Hello Python.")
print()
print("Hello Python")
print()

"""
    2. Write a python program to do arithmetic operations addition and division.
"""

print("2. A python program to do arithmetic operations addition and division")
print()

a = eval(input("Enter number1: "))
b = eval(input("Enter number2: "))

print("Sum of {} and {} is: {}".format(a, b, a+b))
print("Floor Division of {} and {} is {}".format(a, b, a//b))
print("Floating division of {} and {} is {}".format(a, b, a/b))
print()


"""
    3. Write a python program to find the area of triangle
"""

print("3. A python program to find the area of triangle")
print()

base = eval(input("Enter the base value of the triangle: "))
height= eval(input("Enter the height of the triangle: "))

print("Area of the triangle with base: {} and height: {} is: {}".format(base, height, (base* height)/2))
print()



"""
    4. Write a python program to swap two variables
"""

print("4. A python program to swap two variables")
print()

a = eval(input("Enter a first number: "))
b = eval(input("Enter second number: "))

print("Before swapping values are: {} ,{}".format(a, b))
a, b = b, a
print("After swapping values are {}, {}".format(a, b,))
print()


"""
5. Write a Python program to generate a random number
"""
print("A Python program to generate a random number")
from random import random

print(random())