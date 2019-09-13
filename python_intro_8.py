from math import *
from tabulate import tabulate
from psm_plot import *

def lagrange(x,y,xval):
    summ = 0
    prod = 1
    n = len(x)
    for i in range(0, n):
        prod = 1
        for j in range(0, n):
            if i != j:
                prod = prod * (xval - x[j]) / (x[i] - x[j])
        summ += y[i] * prod
    yval = summ
    return yval


def main():
    # place code here to compute eq. 9 as discussed in the sums_and_products.pdf

    # ENGR3703 your code here

    x = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    y = [0.1, 0.08023, 0.02016, -0.08351, -0.23408, -0.43125, -0.66752, -0.92459, -1.16976, -1.35233, -1.4]

    xvals = [0.05,.15,.25,0.35,0.45, 0.55,0.65,0.75,0.85,0.95]
    yvals = []
    for xval in xvals:
        yvals.append(lagrange(x,y,xval))


    TwoScatterColorsPlot111(x,y,"Data",xvals,yvals,"Interpolated Values","x","y","LaGrange Interpolation","lagrange_interp.png")




# please just leave this and don't change it...
# these next two lines make sure main() runs everytime this code file is executed
if __name__ == '__main__':
    main()
