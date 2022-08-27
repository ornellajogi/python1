### TESTING

"""
Software testers
but you yourself should test as well

- everyone makes mistakes
- not every use case will always be foreseen
- in advanced applications, there may be collisions between componenets
- correcting errors early is cheaper than having clients report them (can get sued)
- testing provides info about system components
- testing increases product quality
- avoiding complications after merges

"""

import unittest #package that comes default with Pythin
from test_func import area_of_square # wrong?
import sys
"""
unittest

To write a test case must be wrapped in a class
"""
"""
### code with testing below mixed up as I was away. she modified what was written before
class TestSomething(unittest.TestCase):   #testSmth is a subclass of unittest.Testcase  #rule of thumb, start class with word "Test"
    def test_in_upper(self):   #want to create test runners, methods in test class
        self.assert_()       #code missing

    def test_not_equal(self):
        self.assertNotEqual("Yellow", "Blue")

    def test_is_in(self):
        self.assertIn(3, [7, 4, 5, 6, 3])  #code missing

    def test_is_equals(self):

    def test_is_upper(self):
        txt = "name".upper()

"""

"""
python -m unittest "filename.py" (optional -f ( stops at first fail)
can use green arrow next to test in code to run each
"""

# this runs but not as supposed to
class TestSomething(unittest.TestCase):  # testSmth is a subclass of unittest.Testcase  #rule of thumb, start class with word "Test"
    def test_is_equals(self):
        # check if a == b
        self.assertEqual(10,10)

    @unittest.skip("Skipping example")
    def test_is_equal_fails(self):
        self.assertNotEqual(True, False)
    # self.assert_()  # code missing

    def test_not_equal(self):
        self.assertNotEqual("Yellow", "Blue")

    def test_is_in(self):
        self.assertIn(3, [7, 4, 5, 6, 3])

    def test_is_upper(self):
        txt = "name".upper()
        self.assertEqual("NAME", txt)

    @unittest.skipIf(sys.platform.startswith("win"), "skipping test for windows")
    def test_if_windows(self):  #import sys for this  #if platform = windows, skip test
        self.assertTrue(True)



# can import function from another file and test it here
#but didnt import bc couldnt finish writing the test_func.py

from test_func import area_of_square  #but can't import correctly bc couldnt finish writing the test_func.py

def test_area_of_square(self):  # self doesn't turn purple as should for some reason
    len = 20
    area = area_of_square(len)
    self.assertEqual(area, len*len)

"""
Test Fixture: setUp and tearDown   #To check if connection to database?

setUp = called immediately before your test method.
tearDown = called after your test method is executed.

"""

class TestFixture(unittest.TestCase):
    def setUp(self) -> None:
        print("This is a setup")
        self.list1 = [2,3,4,5,6,7]

    def test_value_in_list(self):
        print("test value")
        self.assertIn(4, self.list1)

    def tearDown(self) -> None:
        print("Tear down")
        del self.list1   # want to destroy the variables created in list after each method

    def test_true_is_true(self):
        self.assertTrue(True)

    def test_exception(self):
        with self.assertRaises(ZeroDivisionError):
            10/0

    def test_exception_name_error(self)
        with self.assertRaises(NameError):

