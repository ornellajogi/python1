######## DONE
"""
Write a program to return the middle value of a list. If there are 2 middle values, return the second


Example: names = ['Ade', 'orange', 'pineapple', 'apples', 'mangoes']
result = 'pineapple'

age = [10, 3, 45, 67, 89.0, 45]
result = 67
"""

names = ['Ade', 'orange', 'pineapple', 'apples', 'mangoes']

"""
NOTES
source: https://dirask.com/snippets/python/python+remove+middle+element+from+list

def remove_middle_index(input_list):
    middle_index = int(len(input_list) / 2)
    del input_list[middle_index]
    return input_list


print(remove_middle_index([1, 2]))  # [1]
print(remove_middle_index([1, 2, 3]))  # [1, 3]
print(remove_middle_index([1, 2, 3, 4]))  # [1, 2, 4]
print(remove_middle_index([1, 2, 3, 4, 5]))  # [1, 2, 4, 5]
"""

names = ['Ade', 'orange', 'pineapple', 'apples', 'mangoes']
print(names)

"""
THIS DOESNT WORK, takes the middle value out, doesnt return it
def remove_middle_index(names):
    middle_index = int(len(names) / 2)
    del names[middle_index]
    return names

print(remove_middle_index(names))

### 2nd part of excercise
age = [10, 3, 45, 67, 89.0, 45]

def remove_middle_index(age):
    middle_index = int(len(age) / 2)
    del age[middle_index]
    return age

print(remove_middle_index(age))
"""


"""
Example that works
list = [1, 2, 3, 4, 5]

middle = int(len(list) / 2) # = int(2.5) = 2
print(list[middle]) # 3
"""

#part 1 of exercise
print(list)
middle = int(len(names) / 2)
print(names[middle])

#part 2 of exercise
age = [10, 3, 45, 67, 89.0, 45]

print(age)
middle = int(len(age) / 2)
print(age[middle])