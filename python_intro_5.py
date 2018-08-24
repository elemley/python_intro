#This is a comment

#The following is the import section
#This brings in other python files that have pre-defined functions in them
#This will be present in every single program you write
from math import *
import numpy as np

#The following area is a sort of "global" area this code will execute first and will always execute

#Below is a function definition
def main():

    #define a variable
    integer1 = 2

    float1 = 1.0

    integer2 = 3

    float2 = 3.0

    #loops!

    # this is a list
    nums = [0.0]

    for i in range(0,10):
        print(i)
        nums.append((i+1)**i)

    print(nums)

    num = 100
    #while(num > 1.1):
     #   num-=1
      #  print(num)

    for i in nums:
        print(i)








if __name__ == '__main__':
    main()











