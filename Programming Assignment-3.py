"""
1. Write a python program to check if a number is positive, negative or zero
"""

x = eval(input("Enter a number to check if a number is positive, negative or zero: "))
if x == 0:
    print("Given number is Zer0")

elif x >0:
    print("Given number {} is positive".format(x))

else:
    print("Given number {} is negative".format(x))


"""
2.Write a python program to check if a given number is even or odd
"""

if (x%2 == 0):
    print("Given number {} is even number".format(x))
else:
    print("Given number {} is odd number".format(x))


"""
3. Write a python program to check Leap year
"""

year = int(input("Enter a year: "))

if year%400 == 0:
    print("Given year is leap year")

elif year %  100 == 0:
    print("Given year is not a leap year")

elif year % 4 == 0:
    print("Given year is leap year")
else:
    print("Given year is not a leap year")


"""
4. Write a python program to check prime number
"""

x = int(input("Enter a number to check prime or not"))
count = 0
for i in range(2, x):
    if x % i == 0:
        print("Given Number is not a prime")
        count = 1
        break

if count == 0:
    print("Given Number is a prime number")

"""
5. Write a program to print all prime numbers in the range 1 to 10,000
"""

for i in range(1, 10000):
    count = 0
    if i == 0 or i == 1:
        count = 1
    for j in range(2, i):
        if i % j  == 0:
            count = 1
            break
    if count == 0:
        print(i, end="  ")