#### DONE
"""
Write a program  that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

hint: use set() =>

list1 = [10, 23, 23, 5, 67, 10]
output = [10, 23, 5, 67]
"""


# Remove duplicate elements from list
def Remove(list1):
    final_list = []
    for num in list1:
        if num not in final_list:
            final_list.append(num)
    return final_list


# Driver Code
list1 = [10, 23, 23, 5, 67, 10]
print(Remove(list1))

