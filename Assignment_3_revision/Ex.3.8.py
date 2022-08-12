##### DONE
"""
Remove all empty strings from a list of strings
hint: use filter() => https://docs.python.org/3/library/functions.html#filter



name_list = ['orange', None, 'pineapple', "", 'apples', 'mangoes','Hello Dear','', 'Hello Sir']
"""
# removing empty strings
# using remove()

# initializing list
name_list = ['orange', None, 'pineapple', "", 'apples', 'mangoes','Hello Dear','', 'Hello Sir']

# Printing original list
print("Original list is : " + str(name_list))

# using remove() to
# perform removal
while ("" in name_list):
    name_list.remove("")

# Printing modified list
print("Modified list is : " + str(name_list))
