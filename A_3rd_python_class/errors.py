"""
Errors terminates the python code being executed

- Syntax error / parser error - error that shouldn't occur, against Python rules
    1exem = 12   #error bc variable cant start with number
    - shows the error with ^
    - most IDE catches this error (integrated dev env)

- Exceptions: errors that occur during execution (breaks)
    - code is syntactically correct
    - but error when trying to execute code

exception handling:
Try: block of code that might return error/ run this code
except: handle the exception
else: lets execute code when there is no error
finally: executes whether an error occurs or not


try:
    print(10/0)
except:
    print("do nothing")   # this prints do nothing, not the error


try:
    print(10/0)
except:
    print("do nothing")   # this prints do nothing, not the error
else:
    print("No error occurred")



try:
    print(10/0)
except:
    print("do nothing")   # this prints do nothing, not the error
else:
    print("No error occurred")
finally:
    print("I occur regardless of an error")


# example: database connection
try: make a connection
catch: error
finally: close the connection

read and write to file
try: read the file
    write to a file
catch: error that occurs during reading of the file
else: close the file

- Logical error - code runs, but you get what not expecting bc smth wrong
"""

"""
1exem = 12

error message:
1exem = 12
     ^
SyntaxError: invalid syntax
"""

"""
print("learning errors"))

    print("learning errors"))
                            ^
SyntaxError: unmatched ')'
"""

"""
### exception error
Traceback (most recent call last):
  File "C:\SDA\python1\A_3rd_python_class\errors.py", line 33, in <module>
    print(10/0)
ZeroDivisionError: division by zero
"""

### TYPES OF Exceptions
"""
Thousands of exceptions

Groups:
- Arithmetic error: e.g. ZeroDivisionError 10/0, cant divide by 0
                        OverflowError - too large (memory, number size ?, max out list/dictionary, run out of range)
- Floating point error (more in C programming language)
- Assertion error: when assertion fails
- Attribute error: when assignment operation fails
- end of file error: when using input function and hits end of file condition
- Import error : from libraries, dont have module ; trouble importing smth
        inside import error have subclasses:
            - module not found error  - import was fine but module inside the import not found
            
                e.g. import module (have python module file, but cant find waht calling)

- Index error: in list,tuple,array... not that index, e.g., have 4 items in list, but call index 7
- Key error: talking about dictionary 
    e.g., dict1 = {"name": "Oyin", "age":28}
            dict1 val1      #dunno which parenthesis she used to call val1
            # means dictionary doesnt contain it
            
- Name error: variable name can't be found
        nt: print(name)    but name doesn't exist
        
"""


### MULTIPLE EXCEPTIONS
"""
Is it possible to have more than 1 exception? YES
How to handle?

try:
    print(name)
except NameError as err:  #named exception
    msg = err
    print(f"a new message: {err}")
except:
    print("other errors")
    
nt: website 404 error, so based on error might want to send different message to users
nt: connecting to database, and run a query, can have connection errors, exceptions, privacy error, etc...
"""


### RAISE EXCEPTIONS

"""
raise exception: basically want to force an exception to occur

nt:
list1 = [10, 4, 5 6, -1, 7, 7]

for x in list1:
    if x < 0:
        raise Exception("negative values shouldn't be in the list")

Outputs:
Traceback (most recent call last):
  File "C:\SDA\python1\A_3rd_python_class\errors.py", line 148, in <module>
    raise Exception("negative values shouldn't be in the list")
Exception: negative values shouldn't be in the list     

   
"""

### Can also create your own exception
"""
Customized exceptions.
When need?
nt: have own code, want people to use it, but have your own set of rules
    nt: Banking: Can't withdraw more money that on checking account if don't have overdraft
        Overdrawn exception
        
How create?
create class, give exception name

class NoNegativeInList(Exception):
    pass
"""

### ÜLESANNE
# do SDA task 10, page 146
"""
Task 10 
Write a program that returns the absolute value of a number retrieved from the user. 
The program should keep asking for this number until it is correctly given. 
Remember that the user may not always enter a numeric value, but may also enter, for example, "cauliflower". 
Check what happens then and be sure to handle exceptions.
"""

### ANSWER
"""
The definition of a program at its most basic is a
sequence of Python statements that have been crafted to do something.
Even our simple hello.py script is a program. It is a
one-line program and is not particularly useful, but in the strictest
definition, it is a Python program.
"""

### should use a while loop
def value_from_user(value_from_user):
    number = abs(value_from_user)
    print(number)

# but this code also gives output "None" if no error, don't know why
# first number entry
try:
    print(value_from_user(-7))

except TypeError as err:  # named exception
    print(f"give number")
else:
    print("Thanks for the number")

# second number entry
try:
    print(value_from_user("cau"))

except TypeError as err:  # named exception
    print(f"give number")
else:
    print("Thanks for the number")
