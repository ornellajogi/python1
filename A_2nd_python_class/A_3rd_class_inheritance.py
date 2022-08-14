"""
Inheritance:
    - inheriting attributes and methods from the base/parent class
    - derived/child class can have it's own attributes and methods

synthax
    class <<ChildClassName>>(BaseClass):
        def __init__(self):
            super().__init__

or

    class <<ChildClassName>>(BaseClass):
        def __init__(self):
            BaseClass().__init__

inside constructor call the XXX of the parent class that want to inherit

good thing about super is don't need to specify parent? class
"""
"""
# create rectangle class
# attributes - length & breadth
# methods - calculate perimeter & area

# gonna hace child class = Parallogram
- inherits from rectangle
- attributes = heights
- volume (going to use formula for perimeter and are from class rectangle)
"""
class Rectangle:
    def __init__(self, len, brd):
        self.length = len  # variable
        self.breadth = brd

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def area(self):
        return self.breadth * self.length

    def show(self):
        print(f"Rectangle Info:\n"
              f"length: {self.length}\n"
              f"Area: {self.area()}\n"
              f"Perimeter: {self.perimeter()}")

# creat object
rect1 = Rectangle(10, 8)
rect1.show()

print("----------------code is at line 50----------------")

class Parallelogram(Rectangle):
    def __init__(self, len, brd, height): #want to pass len, brd, these are parameters
        super().__init__(len, brd)
        self.height = height   # if do self. , can see that have access to all the rectangle stuff in drop down

    def volume(self):
        return self.length * self.breadth * self.height

 #   @classmethod
 #   def show(cls):  # best to use class method, class method benefit = can use to correct your inheritance
 #       cls.show()  # will show what rectangle shows, but will return "Rectangle info..." ehich might not want

        # so instead can do
    def show(self):   # i have show in rectangle and parallellogram, but overwrites base
        print(f"Parallellogram Info:\n"
             f"breadth: {self.breadth}\n"
             f"length: {self.length}\n"   # but here don't need () cause it's an attribute?
             f"Area: {self.area()}\n"
             f"Perimeter: {self.perimeter()}\n"
             f"volume: {self.volume()}\n")  # need () to call a method

para1 = Parallelogram(8, 7, 4)
para1.show()

print("----------------code is at line ----------------")































print("----------------code is at line ----------------")
print("----------------code is at line ----------------")

















print("----------------code is at line ----------------")