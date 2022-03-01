

"""
1. Write a python program to convert kilometers into miles.
"""

kilo = eval(input("Enter kilometer value: "))

miles = kilo * 0.62137119 
print("{} kilometers = {} miles".format(kilo, miles))


"""
2. Write a python program to convert Celsius to Fahrenheit
"""

from calendar import Calendar
from cmath import sqrt


celsius = eval(input("Enter celsius value in degrees: "))

Fahrenheit = (celsius * 9/5 )+ 32

print("{} degrees decelsius = {} degrees Fahrenheit".format(celsius, Fahrenheit))

"""
4. Write a python program to solve quadratic equation
"""

a = eval(input("Enter Co-efficient of x^2 term: "))
b = eval(input("Enter co-efficient of x term: "))
c  = eval(input("Enter co-efficient of constant term: "))

if a ==0:
    print("Given equation is not a valid quadratic equation ")

else:
    discriminat= b**2 - (4*a*c)
    
    print("Root1 = ",(-b + sqrt(discriminat))/(2*a))
    print("Root2 = ",(-b - sqrt(discriminat))/(2*a))
    


"""
5. Write a python program to swap two variables without temp variable
"""

a = eval(input("Enter a first number: "))
b = eval(input("Enter second number: "))

print("Before swapping values are: {} ,{}".format(a, b))
a, b = b, a
print("After swapping values are {}, {}".format(a, b,))
