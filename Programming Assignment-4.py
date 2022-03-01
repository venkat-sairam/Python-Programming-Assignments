"""
1. Write a python program to find the factorial of a number.
"""

x = int(input("Enter a number to find the factorial"))
temp = 1
if x == 0:
    print("the factorial of a number {} is: {}".format(x, 1))
for i in range(1, x+1):
    temp = temp * i
print("the factorial of a number {} is {}".format(x, temp))


"""
2. write a python program to display the multiplication table
"""

for i in range(1, 13):
    print("{} * {} = {}".format(x, i, x * i))


"""
3. Write a python program to print the Fibonacci series
"""

x = int(input("Enter a number to print the Fibonacci series"))
if x < 0:
    print("Cannot print Fibonacci sequence for negative numbers")

a = 0
b = 1

for i in range(1, x):
    c = a + b
    print(c)
    a = b
    b = c


""" 4. Write a program to check Armstrong  Number """

x = int(input("Enter a number to check if Armstrong"))

if x < 0: 
    print("Enter  a positive number")
count_digits = 0
temp = x
while temp>0:
    temp = temp//10
    count_digits+=1
temp = x
out =0
while(temp > 0):
    rem = temp%10
    temp = temp //10
    out = out + pow(rem, count_digits)

if out == x:
    print("Given number is Armstrong  Number")
else:
    print("Given number is not an Armstrong  Number")


"""
    5. Write a python program to find the first Armstrong number in a given interval
"""


x = int(input("Enter starting number in the interval to find the first Armstrong number"))
y = int(input("Enter Last number in the interval to find the first Armstrong number"))
if x < 0 or y < 0:
     print("Enter  a positive numbers")

count = 0
for i in range(x, y+1):
    count_digits = 0
    temp = i

    while temp > 0:
        temp //=10
        count_digits += 1
    temp = i
    output = 0

    while temp > 0:
        rem = temp%10        
        temp //= 10
        output = output  + pow( rem, count_digits)
    
    if output == i:
        print("First Armstrong number in the given interval is: ", output)
        count = 1
        break
if count == 0:
    print("Cannot fing Armstrong numbers in the given interval")


""" Write a python program to find the sum of Natural numbers """


x  = int(input("Enter a natural number to find the sum "))

if x <=0 :
    print("Given number is not a Natural Number")


else:
    count = 0
    for i in range(1, x+1):
        count = count + i

    print("Sum of first {} Natural Numbers = {} ".format(x, count))