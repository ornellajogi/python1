######## DONE
"""
Write a program to find value 20 in the list, and if it is present, replace it with 200.
Only update the first occurrence of an item.

list1 = [5, 10, 15, 20, 25, 50, 20]
"""

list1 = [5, 10, 15, 20, 25, 50, 20]
print(list1)


""""
Notes:
https://www.programiz.com/python-programming/methods/list/index

The index() method returns the index of the specified element in the list.

Example
animals = ['cat', 'dog', 'rabbit', 'horse']

# get the index of 'dog'
index = animals.index('dog')


print(index)

# Output: 1
"""

#find the index of where number 20 is

location_of_20 = list1.index(20)
print(location_of_20)

#REPLACE 20 WITH 200 IN LIST1

"""
Notes:
https://www.geeksforgeeks.org/how-to-replace-values-in-a-list-in-python/

# Replace Values in a List using indexing

# define list
l = [ 'Hardik','Rohit', 'Rahul', 'Virat', 'Pant']

# replace first value
l[0] = 'Shardul'

# print list
print(l)

"""

list1[location_of_20] = 200
print(list1)