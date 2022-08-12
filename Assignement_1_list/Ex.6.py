########## DONE
"""
count number of occurrences of x in the given list

Input : lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
         x = 10
result : 3  #10 appears three times in given list.

Input : lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
        x = 16
result : 0
"""

"""
NOTES

Use .count() to Count Number of Occurrences in a Python List
The easiest way to count the number of occurrences in a Python list of a given item is to use the Python .count() method. The method is applied to a given list and takes a single argument. The argument passed into the method is counted and the number of occurrences of that item in the list is returned.

Let’s see how we can use the .count() method to count the number of occurrences in a Python list:

# Count the Number of Occurrences in a Python list using .count()
items = ['a', 'b', 'a', 'c', 'd', 'd', 'd', 'c', 'a', 'b']
count_a = items.count('a')
print(f'{count_a=}')
# Returns: count_a=3
We can see here that when we apply the .count() method to a list and pass in the item that we want to count, that the number of occurrences are returned.

Let’s see what would happen if we pass in an item that does not exist in the list:

# Count the Number of Occurrences in a Python list using .count()
items = ['a', 'b', 'a', 'c', 'd', 'd', 'd', 'c', 'a', 'b']
count_f = items.count('f')
print(f'{count_f=}')
# Returns: count_f=0
"""


#first part of excercise
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10

count_10 = lst.count(x)
print(count_10)

#second part of excercise
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 16

count_16 = lst.count(x)
print(count_16)










