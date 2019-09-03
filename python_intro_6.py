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
    nums = [-0.2, -1.5, 3.5]  # This makes a list with the first item of 0.0

    # ENGR3703 make a list with 4 floats

    # basic "for" loop
    for i in nums:
        print(i)

    # ENGR make a for loop that iterates the items in your list and prints them

    # if you do the following to a string you can get each character in the string
    for x in "green":
        print(x)

    # to immediately exit a loop use "break"
    for x in nums:
        print(x)
        if x == -1.5:
            break

    # ENGR3703 Loop through your list and make it "break" when you come to the second item

    # you can stop the current iteration of a loop and start with the next with the keyword "continue"
    for x in nums:
        if x == -0.2:
            continue
        print(x)

    # ENGR3703 Loop through your list and make it continue when you come to the third item (note put a print(x) after the continue

    # the range function is handy
    for x in range(5):
        print(x)

    # ENGR3703 use the range function (as above) to print the numbers, 0,1,2,3,4,5,6,7

    # range is handy but sometimes confusing
    for x in range(0, 4):
        print(x)

    # ENGR3703 use the range function (as above) to print the numbers 0,1,2,3,4

    # range can be used with a stepsize also
    for x in range(1, 8, 2):
        print(x)

    # ENGR3703 use the range function (as above) to print the numbers 0,3,6,9,12

    # range can be used with a negative stepsize
    for x in range(10, 0, -2):
        print(x)

    # ENGR3703 use the range function (as above) to print the numbers 21,18,15,12,9

    # something new: else can be used in a for loop
    for x in range(0, 4):
        print(x)
    else:
        print("Done")

    # ENGR3703 use else in a for loop to print numbers 1,2,3 and the message "Finished" after the loop has run

    # loops can be nested
    listoflists = [[1, 3, 5], [-7, 2, 4]]
    for i in range(0, 2):
        for j in range(0, 3):
            print(listoflists[i][j])

    # ENGR3703 as above make a list of lists where there are three lists within a list (each with 4 values)
    # ENGR3703 Use a nested loop to print each item in the following order:
    # ENGR3703 The first item from the first list followed by the first item from the second list etc...

    nums2 = []
    # make a list as you go
    for i in range(0, 10):
        nums2.append((i + 1) ** i)  # This is how you add items to a list

    print(nums2)

    # ENGR3703 make a new empty list with x values: (0, 0.5, 1, 1.5, 2.0)
    # ENGR3703 use a for loop to make another list called y that consists of exp(x) of each of the x vals.

    # Given the flexibility of the for loop, you probably don't need a while loop
    minimum = 5.2
    num = 1.1 * minimum
    while num > minimum:
        num -= 0.02
        print(num)

    # ENGR3703 Make your own while loop example

    # here's a more complicated while loop (common in comp. methods)
    maxiter = 500
    counter = 1
    err_stop = 1e-2
    err = 100 * err_stop
    while err > err_stop and counter < maxiter:
        counter += 1
        err *= .99
    print(err, counter)

    # this loop can be achieved with a for loop also
    err = 100 * err_stop
    for counter in range(0, maxiter):
        if err <= err_stop:
            break
        err *= .99
    print(err, counter + 1)


if __name__ == '__main__':
    main()
