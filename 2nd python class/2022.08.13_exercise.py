"""
Task 1
Write a program that will convert the sequence of numbers entered by the user into text,
e.g .: 112 -> "one one two" 9973 -> "nine nine seven three"
Hint: you need the input () function, a dictionary and a loop.
"""

if __name__ == "__main__":   # wrap into main if want it to run first
    numbers = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }

    user_input = input("give a sequence of numbers \n")
    output_str = ""
    for elem in user_input:
        output_str += numbers[int(elem)] + " "
    print(output_str)


"""
Task 2 Create a function that takes a list of integers and returns what the smallest number is in. 
Do not use built-in functions. eg. for the list [42, 13, 56, 7, 12, 3, 85] the function should return 5, 
because the smallest element is found at this index in this list.
"""


def get_min_index(lst):
    min_value = lst[0]
    min_index = 0

    for idx, value in enumerate(lst):
        if value < min_value:
            min_value = value
            min_index = idx

    return min_index, min_value


if __name__ == "__main__":
    int_list = [42, 13, 56, 7, 12, 3, 85]
    idx, value = get_min_index(int_list)
    print(f"The smallest value in the list is: {value}, it is in position: {idx}")

"""
Task 3 
Create a function that checks that the number given in the argument is prime. 
The function should take a numeric value and return a logical value of True / False. 
E.g. For 11 the function will return True, for 12 -> False.string type 
String supports the same methods that list supports, 
although it is a simple type: 
● len () - number of characters 
● index () - index of the specified character 
● slicing - specifying ranges, eg [3:] ... and some others: 
● startswith () - returns true if the string begins with the given value 
● endswith () - similarly, except end 

● lower () - converts all letters to lowercase 
● upper () - converts all letters to uppercase 
● split () - splits the object into arrays, treating the given string as a separator (by default it is a space) 
● strip () - removes white space 
● join () - joins several strings into one

"""
"""
Task 4 
Create a function that checks if the string given as an argument is a palindrome 
(ie reading backwards and forwards is exactly the same, eg "kayak", "madam").
"""

"""
Task 5 
Create a function that will calculate the number of upper and lower case letters in a string. 
eg for: "The quick Brown Fox" 
expected result: Number of uppercase letters: 3, number of lowercase letters : 13 
Hint: use a loop, conditional statement, and appropriate methods for the string.
"""

"""
Task 6 
Write a function that takes two strings and checks to see if they are anagrams of each other. 
For example: "Army" and "Mary", "Sharing" and "Sunday", \
"Quid est veritas?" and "Vir est qui adest", "Jim Morrison" \
and "Mr. Mojo Risin" "Tom Marvolo Riddle" and "I am Lord Voldemort"
"""