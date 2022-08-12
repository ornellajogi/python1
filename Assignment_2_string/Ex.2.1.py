###### DONE
"""
Write a program to create a new string made of the middle three characters of an input string.

  Example
  input = JhonDipPeta
  result = Dip

"""

#define

def get_middle_three_letters(string1):
    print("Original string is", string1)

# get middle index number
    middle_index_nr = int(len(string1) / 2)

# using string slicing
    res = string1[middle_index_nr - 1:middle_index_nr + 2]
    print("Middle three characters are:", res)

get_middle_three_letters("JhonDipPeta")
get_middle_three_letters("JaSonAy")