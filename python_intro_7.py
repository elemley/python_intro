#This is a comment

#The following is the import section
#This brings in other python files that have pre-defined functions in them
#This will be present in every single program you write
from math import *
import numpy as np

#The following area is a sort of "global" area this code will execute first and will always execute

#Below is a function definition for the main function. This function is meant to hold the code
#that will run every time thhis python code file is executed
#you do have to do something special to make sure it runs though... see the end of the file
def main():

    #now we will learn to take our knowledge of loops to the next level
    #there are some very common problems in comp. methods

    #NOTE: All equations referenced below are in the document sums_and_products.pdf

    #Summations
    #here is an example summation in eq. 1:
    summ = 0
    x = [12, 14, 11, 10, 15, 11]  #define x list
    n= len(x)                   #get length of list
    for i in range(0,n):         #first list index is 0... so the i in the equation we are trying to calc.
        summ+=x[i]               #This loop will execute for i values of 0-5, which correspond to
    print(summ)                  #The six elements in x
    del x

    #ENGR3703 Using what you learned about just above
    #ENGR3703 Write code to calcluate and print a mean value (Eq. 7)
    #ENGR3703 Also write code to calculate a sample standard deviation (see Eq. 8)
    #ENGR3703 Below is the data you should use
    x = [3, 2, 4, 4, 3, 3, 2, 3, 4, 3, 3, 3, 2, 4]

    ##########################################Your code here






    #here is an example summation from eq. 2:
    summ = 0
    n = 10
    for i in range(0,n):
        summ+=(i+1)**3          #here we have to use i+1 since i is being used in the calculation
    print(summ)

    #here is an example summation from eq. 3:
    summ = 0
    n = 10
    a = 2
    for i in range(0,n):
        summ+=a**i              #here we have to use i+1 since i is being used in the calculation
    print(summ)

    #here is an example summation in eq. 4:
    #here we are going to implement a loop that proceeds until the fractional relative error drops below 1e-5
    #The fractional relative error is defined in Eq. 5 (we will use rel_err in the code below)
    f = 0                           #this is the function value we are calculating
    f_old = 0                       #holding place for old value of f in iterations
    err_stop = 1e-5                 #this is what is called the stopping criterion
    rel_err = 1.1*err_stop          #initially make sure rel_err is defined to be more than the err_stop
    max_iter = 1000                 #set a max number of iterations
    x = 1                           #argument of function in Eq. 4
    for i in range(0,max_iter):     #for loop that will execute max_iter times unless there is a 'break'
        f+=pow(x,i)/factorial(i)    #here we have to use i+1 since i is being used in the calculation
        if i > 0:                   #calc rel_err for all iterations but the first
            rel_err = abs((f-f_old)/f)      #calc rel_err
            if rel_err <= err_stop:         #is rel_err less than the err_stop
                print(f, i+1, rel_err)
                break                       #if it is less then stop iterating
            else:                           #if rel_err is still > than err_stop place the current value of f in f_old
                f_old = f                   #the new value of f_old will be used in the next iteration

        print(f,i+1,rel_err)

    #ENGR3703 Place your code here to find the result of Equation 6
    #ENGR3703 Your loop should continue until the relative error is less than 1e-6
    #ENGR3703 Print out the final value of the function, the number of terms require, and the final relative error

    ##########################################Your code here






#please just leave this and don't change it...
#these next two lines make sure main() runs everytime this code file is executed
if __name__ == '__main__':
    main()










