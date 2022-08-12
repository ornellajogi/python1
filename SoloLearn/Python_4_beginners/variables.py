"""
Sololearn:
A variable has a name and a value
To assign a variable use "="
= is called the assignment operator
"""
x = 42
y = "Hello"
z = 3.14
print(x)
print(y)
print(z)

text = "Welcome"
print(text)

"""
naming variables, can't start with number, cant have special characters
CASE SENSITIVE!
    so Lastname and lastname are different
"""
spam = "eggs"
print(spam * 3)

# you can rename variables as much as you want

x = 123.456
print(x)
x = "This is a string"
print(x + "!")

# can use multiple variables together
a = 8
name = "Bob"

print(a * name)

# can use del statement to remove a variable
"""x = 42
del x

    # using deleted variable gives an error
print(x)
"""
#replace variable with var raised to power of 3
num = 7
num = num ** 3
print(num)

"""
some programs need to take input from user.
eg. username and age
input() function prompts user for input, returns what they enter as string

even if enters number, processed as string

on Pycharm doesnt work?
x = input()
print(x)

name = input("Enter your name: ")
print("Hello, " + name)

####

To take input as number use int() function
int() turns string into integer

age = int(input())
print(age)
"""

x = "2"
y = "4"
z = int(x) + int(y)
print(z)

# float() function turns integer into float
"""
height = float(input())
print(height)

just keeps running on Pycharm
"""
x = 9.34
y = int(x)
print(y)  # returns 9

# if need use number in string concatenation, use str() function

age = 42
print("His age is " + str(age))


a = 5
b = 9
x = str(a)
y = str(b)
print(x + y) # returns 59, not 14

# program to take x and y as input and output string x repeated y times
"""
x = input()
y = int(input())
print(x*y)
#these don't print, keep running in Pycharm
"""
###############

# in place operator let you write code like "x = x +3" more concisely as "x += 3"

x = 2
print(x)

x += 3
print(x)

"""
+ (binary)	a + b	Addition	Sum of a and b
- (unary)	-a	Unary Negation	Value equal to a but opposite in sign
- (binary)	a - b	Subtraction	b subtracted from a
*	a * b	Multiplication	Product of a and b
/	a / b	Division	Quotient when a is divided by b.
The result always has type float.
%	a % b	Modulo	Remainder when a is divided by b
//	a // b	Floor Division (also called Integer Division)	Quotient when a is divided by b, rounded to the next smallest whole number
**	a ** b	Exponentiation	a raised to the power of b
"""

# example
x = 9
x %= 2
x += 3
print(x)

# you can also use in-place operators for string concatenation

x = "spam"
print(x)
x += "eggs"
print(x)

# make a program that turns miles into km

"""
miles = int(input())
km = miles * 1.60934

print(km)

(input() keeps running in pycharm
"""

# tip calculator with float as answer











