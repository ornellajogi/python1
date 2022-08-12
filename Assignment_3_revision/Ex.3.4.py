###### DONE
"""
Write a program to reverse row sort in list of lists


list_id = [[4,1,6], [7,9], [8,9,2,4]]
result = [[6,4,1], [9,7], [9,8,4,2]]
"""
# Python3 code to demonstrate
# Reverse Row sort in Lists of List
# using loop

# initializing list
list_id = [[4, 1, 6], [7, 8], [4, 10, 8]]

# printing original list
print("The original list is : " + str(list_id))

# Reverse Row sort in Lists of List
# using loop
for ele in list_id:
    ele.sort(reverse=True)

# printing result
print("The reverse sorted Matrix is : " + str(list_id))