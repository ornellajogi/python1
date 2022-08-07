"""
Task 1.
Reverse a given list in python
info = ['karl', '100', 'Red', 'Mangoes']
"""
info = ["karl", "100", "Red", "Mangoes"]
print(info)
print(type(info))

# reverse list
info.reverse()
print(info)


"""
Task 2.

Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
Hint: use list comprehension with zip function


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result = ['My', 'name', 'is', 'Kelly']

"""
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
print(type(list1))

print(list1)
print(list2)

x = (list1, list2)
print("here")
list(x)
print(list(x))
print(type(x))
print("here1")
zip(list1, list2)
#create tuple with 1 item, put a comma after
tuple1 = ("oranges",)
print(type(tuple1))

tuple2 = ("oranges") #without comma, creates type string
print(type(tuple2))

"""
Add items: convert tuple to a list, append d item and convert back to a tuple
"""

x = list(tuple1)
print(x)
print("hello")
x.append("lemon")
tuple1 = tuple(x)
print(tuple1)

tuple2 = ("star fruit",)
tuple1 += tuple2
print(tuple1)











"""
Task 3.
Write a Python program to find the second largest number in the given list.


Input: list1 = [10, 20, 4]
result: 10

Input: list2 = [70, 11, 20, 4, 100]
result: 70

"""
python second largest item list

"""
Task 4.


"""


"""
Task 5.


"""


"""
Task 6.


"""


"""
Task 7.


"""


"""
Task 8.


"""