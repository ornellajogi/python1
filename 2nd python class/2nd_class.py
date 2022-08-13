"""
Add items to a dict:
- use key_value pair
    <<dict>>.update({

"""
std["is_student"] = "No"
std["name"] = "Oyindolapo"

std.update(
    {
        "best_color": "black"
    }
)
print(std)

new_dict = {
    "height": 160,
    "weight": 65,
    "hair_color": "blond"
}
std.update(new_dict)
print(std)
#std.update("height":160)

"""
remove items in a dictionary:
-pop : generates error if key doesnt exist
<<dict>>.pop(<<key>>)
- popitem() #removes last item of dictionary [-1]
- clear(): empties your dictionary
"""

std.pop("height")
std.popitem()
print(std)

"""
loop through a dict:


"""

for in std: #returns the key or use <dict>.keys()
    print(item, std[item])

for val in std.values(): # returns dict values
    print(val)

for key, val in std.items(): # returns keys and values
    print(f"{key}:{val}")

print(std.items) #she deleted this, was answer

# dictionary comprehension
print(){k:v for k,v in std.items()}) #can switch , name becomes key if instead k:v use v:k
# capitalize values  print({k :str(v).upper() for k,v in std.items()})

"""# nested dictionary / or dictionary for dictionary
<<dict>> = {
<<key>>: {
            >>key>>:<<value>>
            }
<<key>>: {
            <<key>>:<<value>>
            ....
            <<key>>:<<value>>
            }
....
}           
"""
students = {
"Oyindolapo":{
    "is.std": False,
    "age": 28
}
 , "Thomas":
        {
            "is_std": True,
            "age":20
         }
        "Frank":{
            "is.std": True,
            "age":30,
            "hair_color": "red"
    }
}
print(students.keys()) #answer to W, keys have to be unique

# add zip function
#zip helps combine 2 lists

"""
zip:
Easily combine 2 lists
returns list?
"""

name = ["Oyin", "Thomas", "frank", "Imma"]

surname = ["komolafe", "udoh", "White", "Mcneil"]
age = [28, 30, 20, 18]
print(list(zip(name, surname, age)))

# if different lengths, the result will be shortest list

### if else
"""
logical conditions evaluates to boolean = T/F
a ==b {equals}
a != b {not equals}
a < b

"""

if 10 < 5:
    print("less than 5")

else:
    print("not less than 5")

#if multiple conditions

marks = [90, 75,88, 68, 72]

#evaluate
grade = []
for mark in marks:
    if mark <= 98:  =90 -100
         grade.append"A"
        grade.appemd(A+)
    elif mark <= 88:\ and mark < 90: #88 - 89
    grade.append("A+")
    elif park >= 80 and mark < 90 # 80-89
grade.appemd("A")
 elif park >= 70 and mark < 80 # 70-79
grade.appemd("B")
 elif park >= 60 and mark < 78 # 60-69
grade.appemd("C")
    else:
grade.appemd("Fail")

print(grade)

get area_of_square(length):
    return  length



get get shape(len, breatdth):
    if len == breadth:
        area = area_of_square(length=len)
        print(f"Shape is a square with area {area}")
    else:
        print(f"shape is a rectangle with area {area_of_rectangle(len, breadth)}")

get_shape(len=10, breadth=8)
get_shape()

"""
you can have default values for your functions, such that, if no arguments is passed,
the default value is used
"""

#isogram example in lecture
def = isogram(word):
    l = [x for x in word]
    if len(set(l)) == len(l):
        return  True
    else:
        return False

# scrabble example


# class from 14.00
print("text")

"""
File operations:
- creating a file
- reading
- updating
- deleting

"""
"""
#key method for operating file in Python is open()
# takes 2 arguments
# open(<<filename>>, <<mode>>

# 4 basic modes

modes:
r = read => default - opens file for reading, error if file not exist
w = write => open file for writing 
a = append - open the file for appending, if file not exist, creates the file (want to add to existing file)
x = create - create new file, returns error if file exists

difference btwn write and append = write starts from start of file, append adds to the end

2 more modes you can combine:
t = text moden => default mode (so don't need to enter that
b = binary (for images?, convert images into numbers, images into string)

can combine 
"""

# read a file
# can create new file on the left and write smth like "Welcome to Python"

f = open(test.txt) # opens in r t mode because these are default
# this opened for reading (doesnt mean started reading

#now read the file
print(f.read()) # returns everything, but can read line by line

# by line
print(f.readline())
# can use while or for loop to read a long doc

lines = 1
while lines < 10:
    print(f.readline())

# or

while True:
    print(f.readline())
    if not f.readline():   # empty line, then ends?
        break

# to create file use write or append
f = open("test.txt", "a")

# be careful, write writes over your file? so append safer?
f.write("Ohh, it is going to rain. \n The beautiful day is not for outdoor activities") # appending to file
f.close()  # need to close file afterwards

with open("test.txt", "a") as f:
    f.write("\nI won't be able to cycle. \nI think I will paint")


















