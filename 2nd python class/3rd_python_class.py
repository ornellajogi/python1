"""
Q1
given 2 strings, can you make first string from the second by deleting some characters
s1 = "Hello"
s2 = "vufigsaHudesdflelio"

# my ideas on how to solve
there are to e's, so can't just delete all characters apart from Hello
No, I guess don't need to get the word, but True and false
"""

# teachers:
s1 = "Hello"
s2 = "vufigsaHudesdflelio"

def extract_string(string1:str, string2:str) -> str:
    c_string1 = Counter(string1)
    c_string2 =

    intersect =

    if intersect == c_string1

# counter returns dictionary
# counter s2
# from collections return counter
                   count = 0
for ch in s1.lower():
    if ch in s2.lower():
)       count += 1

print(count)
if count == len(s1):
        print("possible")
        print("Not possible")

# Python 3 program to find if it is possible
# to make a string from characters present
# in other string.
MAX_CHAR = 256


# Returns true if it is possible to make
# s1 from characters present in s2.
def isPossible(s1, s2):
    # Count occurrences of all characters
    # present in s2..
    count = [0] * MAX_CHAR
    for i in range(len(s2)):
        count[ord(s2[i])] += 1

    # For every character, present in s1,
    # reduce its count if count is more
    # than 0.
    for i in range(len(s1)):
        if (count[ord(s1[i])] == 0):
            return False
        count[ord(s1[i])] -= 1

    return True


# Driver code
if __name__ == "__main__":

    s1 = "GeeksforGeeks"
    s2 = "rteksfoGrdsskGeggehes"
    if (isPossible(s1, s2)):
        print("Possible")
    else:
        print("Not Possible")

# This code is contributed by ita_c

"""
Q2
sum numbers until flag -9999 is seen
methods
you can save the numbers in a list and compute You can use while loop


MY IDEAS
give list
go through numbers somehow (loop?)
if not -9999
else
"""
def sum_till_minus_9999(list):
    if list == -9999
        sum(list)
        print()

"""
Solutions from online
def sum_until_found(lst, num):
    index = 0
    res = 0
    if num in lst:
        while index < lst.index(num):
            res += lst[index]
            index += 1
    else:
        return "The number is not in the list!"
    return res
Another possible way is:

def sum_until_found(lst, num):
    index = 0
    res = 0
    found = False
    if num in lst:
        while not found:
            res += lst[index]
            index += 1
            if lst[index] == num:
                found = True
    else:
        return "The number is not in the list!"
    return res
There's many ways of doing this without using a while loop, one of which is using recursion:

def sum_until_found_3(lst, num, res=0):
    if num in lst:
        if lst[0] == num:
            return res
        else:
            return sum_until_found_3(lst[1:], num, res + lst[0])
    else:
        return "The number is not in the list!"
Finally, an even simpler solution:

def sum_until_found(lst, num):
    if num in lst:
        return sum(lst[:lst.index(num)])
    else:
        return "The number is not in the list!"
"""
"""
Q3
Find the min and max of set of numbers

my ideas:
there must be a min and max builtin function
what is a set anyway?
A set is created by placing all the items (elements) inside curly braces {} , 
separated by comma, or by using the built-in set() function. 
It can have any number of items and they may be of different types 
(integer, float, tuple, string etc.).
"""

#teachers solution

list1 = [2, 3, 4, 5, 6, -9999, 9, 3, 4]
def sum_number(nums:List) -> float:
    sum = 0
    for x in nums:
        if x != -9999:
            sum += x
        else:
            break
    return sum
# if want to skip over flag, use continue instead of break

def sum_using_args
"""
Q4
Count the number of odd and even elements in a list
"""
#previous q answer
def get_min_mx(*args):
    return min(args), max(args)
get_min_mx(12, 67, -234, )


#odds etc
num_list = []


#2nd version lambda
def_counter_using_lambda(nums:List) ->

def counter_using_dict(nums:List) -> tuple:
    c_nums = Counter

    #link of solutions teacher sends on slack