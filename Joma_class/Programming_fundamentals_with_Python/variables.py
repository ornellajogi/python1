"""
Variables are for storing values
if have f(x)=y
    x = variable

Ex of variable = mouse setting scroll lines

Whenever there is smth that can change, it is a variable

print calls the function print, so print() is a function
you can put input inside your function, that input can be a string or number
another function we learned is type(), put in a number, string, etc, spits out output = class
"""

print("Hello")
print(5)
print(type("I'm a string"))
print(type(True))

"""
Anatomy of a function
picture of it in notes
 
def hello(name):
    greet = "Hi! " + name
    print(greet)
    
hello("Jonathan")

you use def to define function, and the 3 lines are function definition
"""

def hello(name):
    greet = "Hi! " + name
    print(greet)


hello("Jonathan")
hello("rabbit")

def hello1(name):
    greet = "Hi! " + name
    print(greet) # not an output, prints smth on screen
    print("asdf") # that's why can print multiple things
    return name # return keyword means in your function what does it do, what does it return
                # if have return statement, you define what outputting

hello1("Jonson")

# so if do the following, see what function returns
variable1 = hello1("sam")
print(variable1)

print("----------------code is at line 54----------------")

def hello2(name):
    greet = "Hi! " + name
    print(greet) # not an output, prints smth on screen   # these are side effects, return is the output
    print("asdf") # that's why can print multiple things  # these are side effects
    return 50 # can return something completely random

hello2("Paul")

# so if do the following, see what function returns
variable2 = hello2("sam")
print(variable2)

print("----------------code is at line 68----------------")

def tip_amount(tip_percentage, total):
    print("The total is: " + str(total))
    print("The tip % is" + str (tip_percentage * 100) + "%")






print("----------------code is at line ----------------")


print("----------------code is at line ----------------")
print("----------------code is at line ----------------")






print("----------------code is at line ----------------")
print("----------------code is at line ----------------")




print("----------------code is at line ----------------")
print("----------------code is at line ----------------")






print("----------------code is at line ----------------")
print("----------------code is at line ----------------")




print("----------------code is at line ----------------")
print("----------------code is at line ----------------")








print("----------------code is at line ----------------")
print("----------------code is at line ----------------")






print("----------------code is at line ----------------")
print("----------------code is at line ----------------")






print("----------------code is at line ----------------")
print("----------------code is at line ----------------")