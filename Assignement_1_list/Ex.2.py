######## NOT DONE
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