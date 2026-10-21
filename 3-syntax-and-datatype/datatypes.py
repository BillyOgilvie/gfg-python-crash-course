# Strings

# Slicing - syntax is [START:END] - END is EXCLUDED
# You can also pass a option STEP - [START:END:STEP]
# STEP is the interval between indices, with positive
# slicing left to right, and negative slicing right to left
s = "ABCDE"
print(s[1:4])   # print indexes 1-4 BCD
print(s[:3])    # print indexes START-3 ACB
print(s[3:])    # print indexes 3-END DE
# print indexes START-END from right to left in -1 STEPS (reverse string)
print(s[::-1])  # prints EDCBA
#--------------------

# Looping strings
s = "ABCDE"
for char in s:
    print(char)
#--------------------

# String immutability
s1 = "aBCDE"
s2 = "A" + s[1:] # this creates a new string and does not edit the original
print(s1)
print(s2)
#--------------------

# Updating a string
s = "ABCD EF"
s1 = "H" + s[1:]
s2 = s.replace("ABC", "abc")
print(s1)
print(s2)
#--------------------

# Common string methods
# len
s = "GeeksForGeeks"
print(len(s))

# upper & lower
s1 = "Hello World"
print(s.upper())
print(s.lower())

# strip & replace - think of strip like trim in php
s = "   ABC   "
print(s.strip()) # strips white space by default

s1 = "Python is fun"
print(s1.replace("fun", "awesome"))
#--------------------

# Concatenating and Repeating Strings

#--------------------