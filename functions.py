#This is a comment

#The following is the import section
#This brings in other python files that have pre-defined functions in them
#This will be present in every single program you write
from math import *
import numpy as np

#Here is where you can place any functions you might use in your code

def f(x):
    #here is a math function defintition
    tmp = sin(x)/x
    #Now we want to return the value
    return tmp

def area_volume(d):
    #return cross-sectional area and volume of a sphere
    #area = pi/4*d^2
    #volume = pi/6*d^3
    area = pi/4*d**2
    volume = pi/6*d**3
    return area, volume     #you can return area and volume (multiple return values)

def float_list(start,stop,space):
    #return a list that starts with 0, ends with 1, and has spacing of 0.1
    x = []
    n = (int)((stop-start)/space)
    for i in range(0,n+1):
        dx=i*space
        x.append(start+dx)
    return x

def vol_area_ratio(d):
    area,volume = area_volume(d)
    return volume/area

def main():
    #Let's call our function f and print a result
    x = pi/4
    print(f(x))


    print()

    #Now let's make a list of x values
    xlist = [pi/2,3*pi/2,2*pi]      #avoiding zero
    for xval in xlist:
        print(f(xval))

    print()

    #Now let's receive two things
    diam = 30 #cm
    area,volume = area_volume(diam)     #this is how you receive multiple returns from a function
    print("For a diameter of %5.3f cm the area is %5.3f cm^2 and volume is %5.3f cm^3" % (diam,area,volume))

    print()

    #get a float list with start = 0, stop = 1, spacing = 0.1
    print(float_list(0.0,1.0,0.1))

    print()

    #return volume/area (note function calling a function
    print("For a diameter of %5.3f cm the volume to area ration is is %5.3f cm" % (diam,vol_area_ratio(diam)))



#please just leave this and don't change it...
#these next two lines make sure main() runs everytime this code file is executed
if __name__ == '__main__':
    main()










