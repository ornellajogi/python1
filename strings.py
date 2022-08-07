"""
- by default, strings in python are arrays
    -means you can operate each value (each letter by position)
- python doesn't have char data type (like others?-- confusing)
- the first position is 0 for array_like objects
"""
"""
Write python strings.py into terminal to get results there
"""

hello = "Welcome to python"
print(hello[0])
print(hello[4])
print(hello[7]) #returns space

"""
    looping through a string
    for <<variable_name_for_each_char>> in <<string>>:
        statements
"""

for cr in hello:
    print(cr)

"""
    length of a string: len()    #len(<<string>>)
"""
print(len(hello))

"""
    check if a character or phrase exists: in   #in keyword
"""
txt = "it's a beautiful day"
print("beau" in txt)    # will return boolian
print("day" not in txt)

"""
    slicing of strings: <<string>>[<<start_index>>:<<end_index>>]
    slice from a position to end: <<string>>[<<start_index>>:]
    slice from end to a position: use negative index
"""

print(txt[3:7])
print(txt[7:1])
print(txt[-1])  # returns the last char in array
print(txt[-4:-1])

"""
Capitalizing
return to lowercase lower() or casefold()
"""
print(txt.capitalize()) #returns first char as capital letter
print(txt.upper())
print(txt.count("t"))   #returns nr of times char occurs
print(txt.endswith("x"))    #returns true if string ends with specified value

print(txt.find("ful"))  #returns position of this value, if doesn't find, returns -1

"""
string methods 
# look at these: https://docs.python.org/3/library/stdtypes.html
"""
# what is a method? A method is a function. And a function is a block of code.
# if it's within a class, we call it a method, otherwise call function