# This is a comment

# The following is the import section
# This brings in other python files that have pre-defined functions in them
# This will be present in every single program you write
from math import *
import numpy as np

# Here's how you can comment out multiple lines
"""
import time
import matplotlib.pyplot as plt
from psm_plot import *
"""


# The following is a sort of "global" area this code will execute first and will always execute


def main():
    # Notice the indentations... these are used in python rather than things like { }
    print("test")
    # Note the above line may or may not be executed
    print("test2")

    # define a variable
    integer1 = 2
    print(integer1)

    float1 = 1.0
    print(float1)
    print("%5.2f" % float1)

    tmp = float1 / integer1

    integer2 = 3
    print(tmp)
    print(integer1 / integer2)

    print((int)(integer1 / integer2))

    float2 = 3.0
    test = float1 / float2 - 1e-12 * float1 / float2 / 1e-12
    print(test)


print("test")
# Below is a function definition


if __name__ == '__main__':
    main()
