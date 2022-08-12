##### DONE
"""
Replace each special symbol with # in the following string
Hint: import string, and use string.punctuation



import string
string.punctuation



str1 = "%There &are three( students$ and& 1 trainer!"
result = "#There #are three# students# and# 1 trainer#"
"""

import string
str1 = "%There &are three( students$ and& 1 trainer!"
str2 = str1
symbols = string.punctuation

for char in str1:
    if char in symbols:
        str2 = str2.replace(char,"#")
print(str2)