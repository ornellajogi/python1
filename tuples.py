"""
Tuples:
- ordered
- unchangeable
- created/denoted with () #normal brackets
- allow duplicates

"""

#create tuple with 1 item, put a comma after
tuple1 = ("oranges",)
print(type(tuple1))

tuple2 = ("oranges") #without comma, creates type string
print(type(tuple2))

"""
Add items: convert tuple to a list, append d item and convert back to a tuple
"""

x = list(tuple1)
x.append("lemon")
tuple1 = tuple(x)
print(tuple1)

tuple2 = ("star fruit",)
tuple1 += tuple2
print(tuple1)

"""
What makes tuple very powerful?
= unpacking of tuple
means can unwrap a tuple and extract value and assign to variable

the nr of items in tuple should equal to the length of tuple

if not, use * to unpack the remaining to a list
"""

fruit1, fruit2, fruit3 = tuple1
print(fruit2)

#if tuple longer than items assigning it to
# fruit, fruit_2 = tuple1 # gives error: ValueError: too many values to unpack (expected 2)

#this with * doesn't give error
fruit, *fruit_2 = tuple1
print(fruit_2)   #now fruit is string lemon, fruit_2 is a list with lemon and star fruit

print(type(fruit))
print(type(fruit_2))





















































































