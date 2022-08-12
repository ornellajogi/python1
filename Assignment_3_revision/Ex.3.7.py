#### DONE
"""
Remove all characters for string except integers
hint: list comprehension and isdigit()



str1 = "My mum has a 10 year old dog and 2 fishes"
result = 102
"""
# Python code to demonstrate
# to remove all the characters
# except numbers and alphabets

import re

# initialising string
str1 = "My mum has a 10 year old dog and 2 fishes"

# printing initial string
print ("initial string : ", str1)

# function to demonstrate removal of characters
# which are not numbers and alphabets using re
getVals = list([val for val in str1
			if val.isnumeric()])

result = "".join(getVals)

# printing final string
print ("final string", result)


