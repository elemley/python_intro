#This is a comment

#The following is the import section
#This brings in other python files that have pre-defined functions in them
#This will be present in every single program you write
from math import *
import numpy as np

#The following area is a sort of "global" area this code will execute first and will always execute

#Below is a function definition
def main():

    #now we will learn to take our knowledge of loops to the next level
    #there are some very common problems in comp. methods

    #Summations
    #here is an example summation in eq. 1:
    summ = 0
    x = [12, 14, 11, 10, 15, 11]  #define x list
    n= len(x)                   #get length of list
    for i in range(0,n):         #first list index is 0... so the i in the equation we are trying to calc.
        summ+=x[i]               #This loop will execute for i values of 0-5, which correspond to
    print(summ)                  #The six elements in x

    summ = 0
    n = 10
    for i in range(0,n):
        summ+=(i+1)**3          #here we have to use i+1 since i is being used in the calculation
    print(summ)








if __name__ == '__main__':
    main()










