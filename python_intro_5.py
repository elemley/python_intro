# This is a comment

# The following is the import section
# This brings in other python files that have pre-defined functions in them
# This will be present in every single program you write
from math import *
import numpy as np


# The following area is a sort of "global" area this code will execute first and will always execute

# Below is a function definition
def main():
    # this is a list - it's a fundamental data structure in python (it's basically a kind of array
    nums = [0.0, 1.0]  # This makes a list with the first item of 0.0

    print(nums[0])  # Note the index for the list starts with 0
    print(nums[1])

    # ENGR3703 Your Turn to Code
    # ENGR3703 make a new list called numbers, with 4 floats in it.

    # ENGR3703 print the 4th item in the list

    # ENGR3703 print the 1st item in the list

    # A new list and what can be done to it
    strings = ["red", "green", "blue"]

    # Function to determine if a certain value is in the list (use the "in" keyword)
    if "red" in strings:
        print("Found it!")

    # ENGR3703 make a list of 4 strings

    # ENGR3703 Determine if one of the strings that really is there - if so print a message

    # ENGR3703 Determine if one of the strings that really is NOT there - if it's not there print a message

    # Function to get length (number of items) in a list "len"
    print(len(strings))

    # ENGR3703 print the length of your list of strings

    # You can print the entire list like this
    print(strings)

    # Let's append to the list
    strings.append("magenta")
    print(strings)

    # ENGR3703 append a new string to your list of strings

    # to add an item in a particular index
    strings.insert(1, "burnt sienna")
    print(strings)

    # ENGR3703 insert an item into the third position of your list

    # remove an item by the item itself
    strings.remove("magenta")

    # ENGR 3703 remove an item from your list

    # To remove by index use "pop" or "del"
    strings.pop(1)

    # ENGR3703 remove the item in third position in your list

    strings.pop()  # this removes the last item
    print(strings)

    # ENGR3703 remove the last item in your list

    # can also delete this way
    del strings[1]
    print(strings)

    # ENGR3703 delete the first item in your list

    del strings  # totally deletes the list
    # print(strings)

    # ENGR3703 delete your list of strings

    # clear a list but don't delete it
    strings = ["red", "green"]
    print(strings)
    strings.clear()
    print(strings)

    # ENGR3703 remake your original list of strings

    # ENGR3703 clear your list of strings

    for i in range(0, 10):
        # print(i)
        nums.append((i + 1) ** i)  # This is how you add items to a list

    # print(nums)

    num = 100
    # while(num > 1.1):
    #   num-=1
    #  print(num)

    # for i in nums:
    # print(i)


if __name__ == '__main__':
    main()
