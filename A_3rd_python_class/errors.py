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
Try:
except

try:
    print(10/0)
except:
    print("do nothing")   # this prints do nothing, not the error

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
