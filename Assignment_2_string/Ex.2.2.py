########## DONE
"""
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.


    Example:
    s1 = Aunt
    s2 = Sister
    s3 = SisAuntter

"""
def append_middle(s1, s2):

    # find middle index number of s1
    middle_index = int(len(s1) / 2)

    # get character from 0 to the middle index number from s1
    x = s1[:middle_index:]
    # concatenate s2 to it
    x = x + s2
    # append remaining character from s1
    x = x + s1[middle_index:]
    print("After appending new string in middle:", x)

append_middle("Sister", "Aunt")