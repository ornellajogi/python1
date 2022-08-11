############DONE
"""
Concatenate two list
Hint: use list comprehension
<<new_list>> = [expression for item in list1 for y in list2]



list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
"""

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

print(list1)
print(list2)


"""
Notes:
The zip() function returns a zip object, 
which is an iterator of tuples where the first item in each passed iterator is 
paired together, and then the second item in each passed iterator are paired 
together etc.
If the passed iterators have different lengths, the iterator with the least items 
decides the length of the new iterator.

Example:
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)

returns
(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
"""

"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""
print(list1[0])

list3 = [x + y for x in list1 for y in list2]

print(list3)

