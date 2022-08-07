"""
Set:
    - a collection
    - unordered   (list is ordered)
    - unchangeable  (list is changeable)
    - unindexed, you cannot access them through index
    - created/denoted with {}
    - do not allow duplicates (if accidentally put same value, it gets removed)
"""

"""
Write python set.py into terminal to get results there
"""

myset = {"mangoes", "guaves", "berries", "honeydew", "mangoes"}
print(myset)
print(len(myset))

for x in myset:
        print(x)

print("honeydew" in myset)

"""
Add items to a set:
- add <<set>>.add(<<item>>)
- update - adds items from a set into another set
        <<set1>>.update(<<set2>>) 
"""

myset.add("cantalopue")
print(myset)

nuts = {"cashew", "peanut", "almonds", "guavas"}
myset.update(nuts)
print(myset)

# can add list to set
citrus = ["oranges", "tangerine", "lemon", "lime"]
myset.update(citrus)
print(myset)

"""
Removing elements from a set:
        -remove <<set>>.remove(<<item>>)    this generates an error if the item doesn't exist
        - pop: removes the last item in set. But remember that a set is unordered, thus you have no idea/control over what is being removed
        - discard: doesn't return error if item not found
        - clear
"""

myset.remove("guavas")
print(myset)
# myset.remove("passion")        this returns an error bc doesn't exist in set
print(myset)

myset.discard("passion")          #this doesn't return error if item doesn't exist
print(myset)

myset.pop()
print(myset)

"""
Joining of set:
- union: create a new set with item from the 2 sets.
Union also removes duplicates if it occurs.
"""

set1 = {"peanut", "oranges", "berries", "almonds", "cantaloupe"}
print(set1)
set2 = {"cantaloupe", "mangoes", "honeydew", "lime", "tangerine", "lemon"}
print(set2)

set3 = set1.union(set2)
print(set3)

"""
To get common values(duplicates) within a set:
        -intercection >>set1>>.intersection(<<set2>>)
        - intersection_update = what is common to both
"""

set1.intersection_update(set2)
print(set1)

print(set3)
print(set2)

set3.symmetric_difference_update(set2)
print(set3)

print(set3.isdisjoint(set2))   #asking are they completely different, get True or flase














