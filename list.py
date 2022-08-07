"""
    lists are used to store multiple values in a variable
    lists are denoted/created using []
    lists are ordered collection of items
"""
"""
Write python list.py into terminal to get results there
"""

mylist = ["apples", "mangoes", 2, 7.5, "red"]
print(type(mylist))
print(mylist[0])
print(mylist[-1])




# use in to check if value exists in a list
print("guava" in mylist)

"""
Add items to a list
- append: adds to the end of the list
- insert: adds at a specific index
    <<list>>.insert(<<position>>, value)
- extend: appends elements from a list to another list
        <<current_list.extend(<<new_append_list>>)>>
"""

mylist.append("guavas")
mylist.append("grapes")
mylist.insert(2, "blueberries")
mylist.insert(0, "mangoes")
print(mylist)

exotic_fruits = ["cashew", "wild blueberries", "passion fruit"]

mylist.extend(exotic_fruits)
print(mylist)

mylist[4] = "corn"      #replace
print(mylist)

"""
remove items from a list:
    - remove: <<list>>.remove(<<item>>)
    - pop: removes the last item <<list>>.pop()
    - clear: remove all the items in a list
"""
mylist.remove(7.5)
print(mylist)

mylist.pop()
print(mylist)

#duplicate values removal
mylist.remove("mangoes")   # removes 1st value if duplicate
print(mylist)

mylist.remove("apples")
print(mylist)

mylist.insert(0, "mangoes")
print(mylist)

mylist.pop(1)
print(mylist)

exotic_fruits.clear()  # won't delete list, deletes content of list
print(exotic_fruits)

print(mylist)


age = [12, 14, 25, 39, 67, 45 ,13]
print(min(age))
print(min(mylist))

# but if add a number to list
mylist.insert(4, 2)
print(mylist)

mylist.remove(2)
print(mylist)


print(min(age))
print(min(mylist))

mylist.sort()
age.sort()
print(mylist)
print(age)


mylist.sort()
age.sort()
print(mylist)
print(age)


"""
Looping through a list
- for loop
    for <<variable>> in <<list>>:
        statements
- range: allows you to look through a list
"""

ages = str(10)
name = "Oyin"
print(ages)
print(name)

### This code doesnt run for some reason WHYYYYYYYYYYYYYYYY?
#print(f"My name is {name}, I am {ages} years old")
print("My name is "+ name + "I am " + ages + "years old")
print("my name is {} and I am {} years old".format(name, ages))

for var in mylist:
    print(f"I love {var}") # f string
    print("I love " + var)
    print("I love {}".format(var))
######## TILL HERE DOESNT RUN

### didnt run because age wasnt string
# was ages = (10)
#changed to ages = str(10)

"""
solution from online
You are trying to concatenate a string and a number which doesn't work.

You can either convert it to a string before so

usrAge=str(usrAge)

You can do it during print("You are " + str(usrAge) + " years old")

Or you can use a string formatter so Print("You are %d years old"%(usrAge))

I hoped this helped. Any further questions please ask.
"""

for item in age:
    print(item/2)

range(10) # 0 to 9
range(5, 10) # 5 to 9

"""
range(start, stop, step)

default step is 1
"""

for i in range(len(age)):
    print(f"index {i}: {age[i]}")

"""
List comprehension:
    - short method of creating a list
    - short method of creating a list from an existing list
    filter and perform operations
    
    [expression for <<variable_name>> in <<list>> <<optional: condition>>]
"""

x = [print(f"My age is {x}") for x in age]

new_age = [x + 10 for x in age if x%2 == 0]
print(new_age)

# upp_list = [<<expression>> for var in mylist]
upp_list = [var.upper() for var in mylist]
print(upp_list)

# this was a very specific way to write a function.... whatever that means... student's comment

##############################################################################################
##############################################################################################
##############################################################################################

#################################   EXCERCISES  ##############################################
# https://www.w3schools.com/python/exercise.asp?filename=exercise_lists3

fruits1 = ["apple", "banana", "cherry"]
print(fruits1)
fruits1[0] = "kiwi"
print(fruits1)








































