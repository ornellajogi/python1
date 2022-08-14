"""
Object oriented programming
Object has properties and methods.
    An object is an instance of a class

Class is a blueprint for creating objects.

car: class
- minimum size - maximum size
- 4 tyres/wheels
- windows and windshields
- headlamps
- max and min seating
- steering wheel
# these are attributes of a car

different tyoes of a car...

objects: Hyundai, Subaru, Toyota, Mercedes, Tesla, Volvo

different cars follow the same blueprint, have smaller wheel or gear stick closer to driver
but still a car
example of classes and objects

another example

- must have registered of class
- make payment
- signed agreement
- have laptop
- free on weekends

but differences
- taking python
- taking Java

Students: class
- cohort
- course
- location
- method - remote/physical

objects: DS estonia 1, DS estonia 2, Python, Java


Why is class very important?
Why is there object oriented programming
different principles: don't repeat ypurself, if use more than once put in function

Advantage of OOP:
- help you bundle functionalities together(helps you cataloging if need saverage or smth, matclass)
- easy creation of a class instance {object}
once defined class, can make multiple instances of that class
- ability to modify methods of a class without changing the class


"""

"""
● We declare a class using the keyword class. 
After it we write the name of the class (usually in CamelCase style). 
We end the declaration with a colon. 

● After the colon in the indented block, we write the body of the class. 
A class can consist of two main elements: 
○ methods -functions defined in the body of the class, 
most of which will have a special first argument: self. 
○ attributes - variables of any type defined in the class body or in its constructor (__init__).
"""
class Car:
    def __init__(self, name, num_doors=4, exotic = False):
        self.name = name
        self.door_no = num_doors
        self.is_exotic = exotic
        self.in.motion = False

    def doors(self): #now giving methods. To modify attributes?
        if self.door_no not in [2, 3, 4]:
            return f"{self.name} has invalid door numbers"
        return self.door_no



# constructor is executed when class called
# first thing executed, helps assign values to your properties at point of creation



