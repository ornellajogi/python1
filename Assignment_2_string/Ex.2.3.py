##### DONE
"""
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.


    Example:
    s1 = America
    s2 = Japan
    s3 = AJrpan
"""

def mixed_string(s1, s2):
    # getting 1st character from s1 and s2 strings
    first_character = s1[0] + s2[0]

    # getting the middle character from s1 and s2 strings
    middle_character = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]

    # getting the last character from s1 and s2 strings
    last_character = s1[len(s1) - 1] + s2[len(s2) - 1]

    # add all
    res = first_character + middle_character + last_character
    print("Mixed String is ", res)

s1 = "America"
s2 = "Japan"
mixed_string(s1, s2)
