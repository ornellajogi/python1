"""
python
    - create a function inside another function
    - pass a function as an argument to another function
A decorator is a function that takes another function and extends the behaviour of the latter function without
explicity modifying it

"""

def increment_num(num):
    return num + 2

print(increment_num(3))

"""Using a function as an argument"""

def welcome_student(name):
    return f"Welcome {name} from the break"

def did_you_study(name):
    return f"I hope you studied {name}"

def greetings(any_func):
    return any_func("Oyin")

print(greetings(did_you_study))
print(greetings(welcome_student))


"""
create a function within another function - nested functions
- inner functions are not defined until the parent function is called/executed
- inner function is local to your function, hence they are not available outside the parent
"""

def outer_box():
    print("This is the parent box")

    def middle_box(): #inner function
        print("This is the middle box")

    def last_box(): #inner function
        print(("This is the last one".upper())


###"""
###function creating another function
###"""
## this gives error, but in file decorators 2 it works
def greeting(hour):
    def morning(name):
        return f"Good morning {name}"

    def afternoon(name):
        return f"Good aft {name}"

    def evening(name):
        return f"Good eve {name}"

    def night(name):
        return f"Good night {name}"

    if hour < 12:
        return morning
    elif hour >= 12 and hour < 17:
        return afternoon
    elif hour >=17 and hour < 20:
        return evening
    else:
        return night

greet = greeting(14)
print(greet("Oyin"))










