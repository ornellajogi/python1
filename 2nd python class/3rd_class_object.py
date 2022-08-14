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
    accelerate = 15 # class variables use for e.g. if PMI doesn't change, in Europe 25, if use flag like -9999 in exercise above
    def __init__(self, name, num_doors=4, exotic = False):
        self.name = name
        self.door_no = num_doors
        self.is_exotic = exotic
        self.in_motion = False
        self.speed = 0

    def get_doors(self): #now giving methods. To modify attributes?
        if self.door_no not in [2, 3, 4]:
            return f"{self.name} has invalid door numbers"
        return self.door_no

    def drive(self):            #can have method call drive
        self.in_motion = True # when start driving = true

    def acceleration(self, acceleration= 10): # only speed up once in motion...weird logic
        if self.in_motion:
            self.speed += acceleration

    def stop(self):
        self.in_motion = False

"""
Constructor 
● The __init__ special method is called by Python when creating a new class object. 
● As the name suggests, it is used to initialize an object - for example, assigning initial values to attributes,
establishing a database connection, or other activities that should only be performed once, 
at the beginning of a new object's life. ● The __init__ method, like any other method, 
takes self as its first argument. self, is a reference to a specific class object. 
● Like other methods, __init__ can take additional parameters - in our case it is the 
registration number of the created vehicle.
"""

"""
Methods 
● Note that methods often modify attributes object. 
In our case, one method increases the speed and the other resets it. 
● These methods take no arguments in addition to a reference to the current object (self). 
However, nothing prevents them from accepting more arguments. 
● It is similar with the return value - since our methods modify the internal state 
of the object (speed) they don't need to return anything, but of course each method is 
really a function and therefore can return a value using the return keyword.
"""

# CREATING OBJECTS

car1 = Car(name="Toyota Prius", num_doors=4)
car2 = Car(name="Tesla A20", num_doors=2, exotic=True)

print(car1)
print(car1.get_doors())
print(car2.get_doors())

# constructor is executed when class called
# first thing executed, helps assign values to your properties at point of creation

car2.drive()
car2.acceleration(30)
print(car1.speed)
print(car2.speed)
# speed is variable so no curly bracket? acceleration is a method
# have modified acceleration for car 2, for car 1 zero?

# declaring instance variables...missed her talk
# class variables declared and shared between all instances
# instance variable unique to each


"""
CLASS METHOD

Class method:
    - called on class itself, not on an object instance
    - can only access your class variables
    <<class>>.<<class_method>> 
"""

class Student:
    def __init__(self, name, age, cohort):
        self.name = name # variables
        self.age = age
        self.cohort = cohort

    def print_std(self):
        print(f"name: {self.name}\nage: {self.age}")

std1 = Student("name", 28, "DSI1")


