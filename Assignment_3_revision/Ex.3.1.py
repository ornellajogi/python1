###### DONE
"""
read function range()
https://docs.python.org/3/library/stdtypes.html#range


Reverse the order of words in a given sentence.

str_val = "Hello World"
output = "World Hello"
"""

"""
NOTES
Dictionaries and dictionary views are reversible.

>>>
>>> d = {"one": 1, "two": 2, "three": 3, "four": 4}
>>> d
{'one': 1, 'two': 2, 'three': 3, 'four': 4}
>>> list(reversed(d))
['four', 'three', 'two', 'one']
>>> list(reversed(d.values()))
[4, 3, 2, 1]
>>> list(reversed(d.items()))
[('four', 4), ('three', 3), ('two', 2), ('one', 1)]
Changed in version 3.8: Dictionaries are now reversible.
"""

"""
Notes from: https://www.geeksforgeeks.org/print-words-string-reverse-order/
"""


# Print reverse of words in a string.


def wordReverse(str):
    i = len(str) - 1
    start = end = i + 1
    result = ''

    while i >= 0:
        if str[i] == ' ':
            start = i + 1
            while start != end:
                result += str[start]
                start += 1
            result += ' '
            end = i
        i -= 1
    start = 0
    while start != end:
        result += str[start]
        start += 1
    return result


# Driver Code
str = 'Hello World'
print(wordReverse(str))
