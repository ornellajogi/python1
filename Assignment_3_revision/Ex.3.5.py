###### DONE
"""
Write a program to pair elements with rear element in matrix row


list1 = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
result = [[[4, 6], [5, 6]], [[2, 5], [4, 5]], [[6, 5], [7, 5]]]
"""

# Pair elements with Rear element in Matrix Row
# using list comprehension

# Initializing list
list1 = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]

# printing original list
print("The original list is : " + str(list1))

# Pair elements with Rear element in Matrix Row
# using list comprehension
res = []
for sub in list1:
    res.append([[ele, sub[-1]] for ele in sub[:-1]])

# printing result
print("The list after pairing is : " + str(res))