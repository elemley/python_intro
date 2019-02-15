#This is a comment

#The following is the import section
#This brings in other python files that have pre-defined functions in them
#This will be present in every single program you write
from math import *
import numpy as np

def fprime(x,k):
    if k == 0:
        return sin(x)
    if k == 1:
        return cos(x)
    if k == 2:
        return -sin(x)
    if k == 3:
        return -cos(x)

def main():
    #here is the solution to hw 2 problem 1
    #here we are going to implement a loop that proceeds until the absolute error drops below 1e-6
    x0 = pi/12                      #base-point for expansion
    x = pi/2                        #where we want sin(x) eval
    h = x - x0
    fapprx = 0.0                      #this is the function value we are calculating
    ftrue = sin(x)                  #set ftrue here -- it will not change
    err_stop = 1.3e-15                 #this is what is called the stopping criterion
    true_err = 1.1*err_stop         #initially make sure rel_err is defined to be more than the err_stop
    max_iter = 100                  #set a max number of iterations
    for i in range(0,max_iter):     #for loop that will execute max_iter times unless there is a 'break'
        k = (i+4)%4                     #this gives us an index we can use to figure out fprime
        #Taylor series = sum f^i(x0)*h^i/i!
        fapprx+=fprime(x0,k)*h**i/factorial(i)        #here we have to use i+1 since i is being used in the calculation
        true_err = abs((ftrue-fapprx)/ftrue)      #calc true_err
        if true_err <= err_stop:         #is rel_err less than the err_stop
            print(fapprx, i+1, true_err)
            break                       #if it is less then stop iterating
        print(fapprx,i+1,true_err)


#please just leave this and don't change it...
#these next two lines make sure main() runs everytime this code file is executed
if __name__ == '__main__':
    main()










