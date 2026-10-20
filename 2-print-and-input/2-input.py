"""
By default, input() always returns data as a string,
even if you enter numbers. If you want other types like integer (int)
or floating-point (float), you have to convert (typecast) the value
explicitly.
"""

# Basic usage --
# a = input("What colour is the rose? ")
# print("The rose is", a)
#--------------------

# taking input as an int --
# n = int(input("How many roses? "))
# print("Total roses:", n)
#--------------------

# taking input as a float --
# p = float(input("Price of each rose? "))
# print("Price entered:", p)
#--------------------

# taking multiple inputs --
# x, y = input("Enter two numbers separated by a space ").split()
# print("First number:", x)
# print("Second number:", y)
#--------------------

# name and age input --
# name = input("Please Enter Your Name: ")
# age = input("Please Enter Your Age: ")
# print("Name and Age:", name, age)
#--------------------

# adding two numbers --
# n1 = int(input("First number: "))
# n2 = int(input("Second number: "))
# sum = n1 + n2
# print("Sum of two numbers is:", sum)
#--------------------

# taking lists as input --
"""
Note, there is no cast to int here, if if the user enters:
    List1: 123
    List2: 465
Those are strings - "123" and "456". Then when list() iterates over those,
we get
    a = ["1", "2", "3"]
    b = ["4", "5", "6"]
"""
a = list(input("List1: "))
b = list(input("List2: "))
for i in b:
    a.append(i)

print("Final List:", a)
#--------------------