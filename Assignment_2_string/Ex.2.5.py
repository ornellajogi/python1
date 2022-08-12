####### HALF DONE
"""
Write a program to split a given string on hyphens and display first and last substring.


    str1 = Emma-is-a-data-scientist
    result = Emma, scientist
"""


#display each substring
str1 = "Emma-is-a-data-scientist"

new_str = str1.split("-")
print("Displaying each substring")
for word in new_str:
    print(word)

# display first and last substring
def Convert(string):
    li = list(string.split("-"))
    return li

print("printing_from_here")  #to know where I am in code

# Driver code
str1 = "Emma-is-a-data-scientist"
print(Convert(str1))
split_list = (Convert(str1))
print("printing_from_here_1")  #to know where I am in code
print(split_list)


print("printing_from_here_2")  #to know where I am in code
print(split_list[0], split_list[-1])
