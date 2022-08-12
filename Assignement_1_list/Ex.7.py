###### DONE
"""
write a program to remove all occurrences of item 20
Hint: list comprehension

list1 = [5, 20, 15, 20, 25, 50, 20]
"""

list1 = [5, 20, 15, 20, 25, 50, 20]

print(list1)

"""
NOTES
https://www.programiz.com/python-programming/methods/list/remove

Python List remove()
In this tutorial, we will learn about the Python List remove() method with the help of examples.

The remove() method removes the FIRST matching element (which is passed as an argument) from the list.

Example
# create a list
prime_numbers = [2, 3, 5, 7, 9, 11]

# remove 9 from the list
prime_numbers.remove(9)


# Updated prime_numbers List
print('Updated List: ', prime_numbers)

# Output: Updated List:  [2, 3, 5, 7, 11]
"""

"""
THIS DOESNT WORK, ONLY removes FIRST occurrence
#remove all 20s from list

list1.remove(20)
print(list1)

gives
[5, 15, 20, 25, 50, 20]
"""

"""
You can use a list comprehension:

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

x = [1, 2, 3, 4, 2, 2, 3]
x = remove_values_from_list(x, 2)
print x
# [1, 3, 4, 3]
"""

#remove all 20s from list

def remove_all_20_from_list(the_list, val):
   return [value for value in the_list if value != val]


list1 = remove_all_20_from_list(list1, 20)
print(list1)