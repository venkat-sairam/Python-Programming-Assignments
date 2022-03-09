"""
1. Write a Python program to check if the given number is a Disarium Number
"""
def checkDisarium(n):
    
    len_n = len(n)

    temp = int(n)
    summation = 0

    while temp >0:
        
        summation += pow(temp % 10, len_n)
        temp //= 10
        len_n -=1

    return 0 if summation == int(n) else -1

ret_val = checkDisarium(input("Enter a number to check if disarium number or not: "))
if ret_val == 0:
    print("Given number is a Disarium number")
else:
    print("Given number is not a disarium number")
    

print()
"""
2. Write a Python program to print all the Disarium Numbers from 1 to 100
"""

for i in range(1, 101):
    if(checkDisarium(str(i)) == 0):
        print(i)


"""
3. Write a program to check if a given number is Happy Number
"""
print()
def checkIfHappyNumber(x):
    summation = x
    if x == 1 or x == 7:
        return 1
    while summation > 9:
        summation = 0
        while x > 0:
            summation += pow(x%10, 2)
            x //=10

        x = summation
        
        if x == 1:
            return 1
            
    if x == 7:
        return 1

    return 0

x = int(input("Enter a number to check if Happy number or not: "))
if checkIfHappyNumber(x) == 1:
    print("Happy Number")

else:
    print("Not a Happy Number")


print()
"""
4. Write a Python program to print all happy numbers between 1 and 100? 
"""
print("Happy Numbers between 1 and 100 are: ")
for i in range(1, 101):
    if checkIfHappyNumber(i) == 1:
        print(i, end=" ")
    
print()
"""
5. Write a program to check Whether the given number is a Harshad Number
"""

x = int(input("Enter a number to check whether the given number is a Harshad Number or not:  "))

temp = x
summation = 0
while(temp > 0):
    summation += temp % 10
    temp //= 10

if x % summation == 0:
    print("Given number is Harshad Number")    

else:
    print("Given number is not Harshad Number")

