"""
A module can be deduced as a library
Each python file ".py" is treated as a module
"""
import pip

"""
if want someone's code from another file
that's why have modules 

import <<filename>>  # imports everything from a file
# common examples
    import os
    import math

import <<filename>> as <<alias>>  # renaming the model
# common examples
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from <<filename>> import <<Class, function>> # import specific items
    from collections import Counter
    
"""

# from A_3rd_class_inheritance perimeter   # doesn't work for some reason

#need to rename files to start with letter :(

from lib.testmod import laskdlks # to import from upper directory...or other folder
# creating empty file __init__.py   makes the folder a package

# pip install pandas to download package

# if want to share a project and make it run on someone else's computer, put installed package & environment?
# there is a thing called the environment file, it includes all dependeces needed

pip freeze > requiements.txt
# creates requirements file that includes all info, includes also all versions

#python comes with libraries pip, setuptools, wheel (without it can't use)
# to know the packages I use
















































































































