######### DONE

"""Write a Python program to find the second largest number in the given list.


Input: list1 = [10, 20, 4]
result: 10

Input: list2 = [70, 11, 20, 4, 100]
result: 70
"""
list1 = [10, 20, 4]
print(list1)
#sort list
list1.sort()
print(list1)

#find 2nd largest number
print(list1[-2])

list2 = [70, 11, 20, 4, 100]
print(list2)

#sort list
list2.sort()
print(list2)

#find 2nd largest number
print(list2[-2])