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
  #  print("The total is: " + str(total))   # removed bc if input this function's return to next, repeats
  #  print("The tip % is " + str (tip_percentage * 100) + "%") # removed bc if input this function's return to next, repeats
  #  print("The tip amount will be: " + str(total * tip_percentage)) # removed bc if input this function's return to next, repeats
    return total * tip_percentage  # without return, next function can't take result of this

tip_amount(0.15, 100)

# can also do

potato = 100

tip_amount(0.15, potato)

tip_amount(0.54, potato)

"""
functions are also good for organization. can call other functions
"""

def buy_produce(num_of_tomatoes: object, num_of_bananas: object, num_of_potatoes: object) -> object:
    total_price = num_of_tomatoes * 2.00 + num_of_bananas * 1.5 + num_of_potatoes * 3.00
    print("Welcome to Joma Groceries")
    print("Today you bought: ")
    print(str(num_of_tomatoes) + " tomatoes")
    print(str(num_of_bananas) + " bananas")
    print(str(num_of_potatoes) + " potatoes")
    print("Your total is: $" + str(total_price))
    tips = tip_amount(0.15, total_price)
    print("Please tip me $" + str(tips))
    tips_more = tip_amount(0.4, total_price) # can reuse that function, and just add more stuff
    print("If you're feeling generous, give me " + str(tips_more))

buy_produce(4,4,4)

# to have 2nd function be able to use previous function, can't just use print in the first one. Need to use return()
# otherwise here rerutns tips as None

print("----------------code is at line 108----------------")

"""
Problem 1: Score
Let’s say that every day in JomaClass (fictional school) you get a quiz. You can either get the
correct answer, the wrong answer or not do the quiz at all because you slept through your alarm
and didn’t show up to class. Each of them will have a different score:
● Correct answer: 2 points
● Wrong answer: 1 point
● Didn’t show up: 0 points
Write a function that produces your final score as a percentage given:
● total : the number of quizzes
● correct : the number of quizzes you correctly answered
● wrong: the number of quizzes you answered incorrectly.

def score (total, correct, wrong):
# your code here
return
"""
def score(total, correct, wrong):
    points = (correct * 2) + (wrong *1)
    total_points = total * 2
    print((points/total_points)*100)
    return (points/total_points)*100

# wrote this by myself :D

score(20,20,0)
score(20,15,0)
score(20,15,5)
score(20,10,5)
score(20,0,20)


print("----------------code is at line 142----------------")


"""
PROBLEM 2

Problem 2 (Challenge): Score of best 75% days
The same question as previously, however, we only take your best 75% days to account for sick
days. No one is ever healthy every day. That means that even if they didn’t get every question
correct, as long as they got 75% of the questions correct, they will get 100%. See the example
outputs below.
Write a function that produces your final score as a percentage given:
● total : the number of quizzes
● correct : the number of quizzes you correctly answered
● wrong: the number of quizzes you answered incorrectly.

def score75 (total, correct, wrong):
# your code here
return
"""

def score75(total, correct, wrong):
    points = (correct * 2) + (wrong * 1)
    total_points = total * 2
    find_25_pc = total * 0.25
    print(find_25_pc)

    remove_25_pc = wrong - find_25_pc
    print(remove_25_pc)

    list_points = [correct * 2]
    print((points/total_points)*100)
    return (points/total_points)*100

score75(20,15,5)


# below one copied, don't understand how works
def score75_2(total,true,false):
    n_true = min(true,0.75*total)
    print(n_true)
    n_false = min(false,0.75*total-n_true)
    print(n_false)
    n_score = score(0.75*total, n_true, n_false)

score75_2(20,10,5)







print("----------------code is at line ----------------")