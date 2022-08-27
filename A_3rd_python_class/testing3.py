import unittest #package that comes default with Pythin
from test_func import area_of_square  #but can't import correctly bc couldnt finish writing the test_func.py

#doesn't run some code before missing? took this part of code from testing.py
Class TestSomething(unittest.TestCase):
    def test_area_of_square(self):  # self doesn't turn purple as should for some reason
        len = 20
        area = area_of_square(len)
        self.assertEqual(area, len*len)