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

    #Logic and relational operators

    # Operators:
        # <  less than
        # >  greater than
        # <=  less than or equal to
        # >=  greater than or equal to
        # == equal to
        # != not equal to
        # and / or / not

    print(2>1)
    print(1>2)
    print(2>1 or 1>2)
    print(2 > 1 and 1 > 2)
    print(not (2>1))
    print(1 == 2)
    print (1 != 2)











    #do a calculation
    #test2 = pow(float2,3.0)
    #print(test2)
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






if __name__ == '__main__':
    main()











