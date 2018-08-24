#This is a comment

#The following is the import section
#This brings in other python files that have pre-defined functions in them
#This will be present in every single program you write
from math import *
import numpy as np

#Here's how you can comment out multiple lines
"""
import time
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import colors
from psm_plot import *
from random import *
from time_step_scrolling import *
"""
#The following is a sort of "global" area this code will execute first and will always execute


print("test")

#Below is a function definition
def main():

    #define a variable
    integer1 = 2

    float1 = 1.0

    integer2 = 3

    print((int)(integer1/integer2))

    float2 = 3.0

    #do a calculation
    test2 = pow(float2,3.0)
    print(test2)

    print(pow(27,1/3))

    #can also use ** for exponentiation
    print(27**(1/3))

    #parentheses are evaluated first
    print((1+1)**(5-2))

    #exponentiation is always done next
    print(2**1+1)
    print(3*1**3)

    #multiplication and division are always before addition/subtraction
    print(2*3-1)
    print(5-2*2)
    #mult. and div. have same level of precedence - they are done left to right
    #add. and subtract. have same level of precedence - they are done left to right

    #Some different operators
    



    print(16-2*5)





"""
    #do some logic
    if(integer1>integer2):
     #   print("%d is larger than %d" % integer1, integer2)
    #else:
    #    print("%d is larger than %d" % (integer2, integer1))

    if(float2 > float1 and integer2 > integer1):
#        print("%d is larger than %d and %3.2f is larger than %3.2f" % (integer2, integer1,float2,float1))

    if(integer1<integer2):
 #       print("%d is smaller than %d" % (integer1, integer2))
    elif(float1<float2):
  #      print("%3.2f is smaller than %3.2f" % (float1, float2))
    else:
        "None of the above"

"""





    #do a loop



if __name__ == '__main__':
    main()











