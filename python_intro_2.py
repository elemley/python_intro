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

print("test")


# Below is a function definition
def main():
    # define a variable
    integer1 = 2

    float1 = 1.0

    integer2 = 3

    print((int)(integer1 / integer2))

    float2 = 3.0

    # do a calculation
    test2 = pow(float2, 3.0)
    print(test2)

    print(pow(27, 1 / 3))

    # can also use ** for exponentiation
    print(27 ** (1 / 3))

    # Operators:
    # + - * / // %
    # + = addition
    # - = subtraction
    # * = multiplication
    # / = division
    # // = floor division (performs integer division -- 3/4 = 0, 4/3 = 1
    # % = modulus -- divides and returns the remainder -- 3%4 = 3 --- 10%3 = 1

    # parentheses are evaluated first
    print((1 + 1) ** (5 - 2))

    # exponentiation is always done next
    print(2 ** 1 + 1)
    print(3 * 1 ** 3)
    # when you have two or more exponentiations they go right to left

    # multiplication and division are always before addition/subtraction
    print(2 * 3 - 1)  # what will the answer be??
    print(5 - 2 * 2)  # what will the answer be??

    # mult. and div. have same level of precedence - they are done left to right
    # add. and subtract. have same level of precedence - they are done left to right

    print(16 - 2 * 5)  # what will the answer be??
    print(2 ** 2 ** 3 * 3)  # what will the answer be??

    # math library functions
    print(pi)
    print(sin(pi / 2))
    print(cos(pi / 4))
    print(2 * asin(1))
    print(tan(pi / 4))
    print(exp(1))
    print(e)
    print(log10(100))
    print(log(1.0, exp(1)))
    print(log(1.0))
    print(sqrt(25))

    # get log of 1+x with log1p(x)
    tmp = 1e-100 + 1
    print(log(tmp))
    print(log1p(1e-100))

    print(sin(radians(270)))
    print(degrees(atan(1.0)))
    print(cosh(0), sinh(0))
    print(erf(1.0))


if __name__ == '__main__':
    main()
