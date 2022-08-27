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


"""
decorator
- takes a function as an argument
- defines an inner function
- returns the function as a result of its operation
"""

def my_decorator(func):  #dec takes function as argument?
    def wrapper():
        print(f"This is my wrapper")
        func() #print function Im returning
    return wrapper

def say_cheese():
    print("python is fun")

#print(my_decorator(say_cheese()) #pass say cheese into decorator?
my_decorator(say_cheese)()  #parenthesis after because it calls smth?

# or I can use
@my_decorator
def say_something():
    print("saying smth")

say_something() #if i call say smth, it should activate wrapper
#instead lines 40-44, I can use @ say smth


def increment(func):                   #wrapper is taking the arguments of the function
    def wrapper(*args, **kwargs): #args and kwargs are habituary arguments? named or non-named arguments can use these.
        num = sum([x**2 for x in args])  #increments decorator which is performing an action; x**2 squares
        num2 = sum([x+2 for x in args])  #idea is that inside decorator can perform any ...?
        return func(*args, **kwargs)
    return wrapper

@increment
def just_a_num(num):
    return num + 3

@increment
def two_nums(num1, num2):
    return num1 + 3, num2 + 3

#print(just_a_num(5))
print(two_nums(10, 8))


# meaning of stars in front of args and kwargs

"""
a, b, c = (10, 3, 6) # this automatically gives 10 to a, 3 to b, etc.
a, b = (10, 3, 6)  # this would give error, bc 3 inputs wants 3 outputs
a, b, c = (10, 3, 6) : *args    # n number of arguments , one * is positional
a, b, c = (10, 3, 6) : *args == positional arguments (dont need named argument)

**kwargs == named arguments
num1 = 3, num2 = 10, num3 = 6 

thats the difference btwn args and kwargs

positional comes before named
if combine positional and named arguments
"""

#e.g. of positional arguments
def some_example(val1,val2,val3):
    print(val1)
    print(val2)
    print(val3)
    print("doing smth")

some_example(10, 3, 7)
some_example(val2 = 10, val3 = 6, val1 = 8)  # named arguments

# can combine both, but if combine, positional should come before named
some_example(8, 7, val3=17)
# cant do this line below bc positional after named
# some_example(8, val3=17, 7)


# if use args can do this instead of last
def some_example(*args):
    for x in args:
        print(x)
    print("doing smth")

some_example(10, 3, 7)
some_example(2,3,4,5,6,7,8) # can do this

# can combine both, but if combine, positional should come before named
# some_example(8, 7, val3=17)
