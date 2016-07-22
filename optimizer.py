"""
 1.Find minimum values of  functions
 2.Build parameterized models based on data
 3.Refine allocations to stocks in profolio

"""

"""Minimize on objective function,using Scipy"""

"""
How to use an optimizer ? Three steps.

1) Provide a funcion to minimize 
2) Provide an initial guess
3) Call the optimizer
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def f(X):
    """Given a scalar x, return some value.(a real number)"""

    Y = (X-1.5)**2 +0.5

    print "X={}, Y={}.".format(X,Y) # for tracing

    return Y
    
def error(line,data):
    
    """
    Compute error between given line model and observed data
    
    Parameters
    --------------------
    line: tuple/list/array (C0, C1) where C0 is slope and C1 is Y-intercept
    data: 2D array where each row is a point(x,y)
    
    Returns error as a single real value.
    
    """
    
    err = np.sum(data[:,1]-line[0]*data[:,0]-line[1])**2
    
    return err
    
    
def test_run():
    Xguess=2.0
    min_result=spo.minimize(f,Xguess,method='SLSQP',options={'disp':True})
    print "Minima found at:"
    print "X = {}, Y = {}".format(min_result.x,min_result.fun)
    # plot function values , mark minima
    Xplot = np.linspace(0.5,2.5,21)
    Yplot = f(Xplot)
    plt.plot(Xplot,Yplot)
    plt.plot(min_result.x,min_result.fun,'ro')
    plt.title("Minima of an objective function")

    plt.show()
if __name__=='__main__':
    print "begins"
    test_run()

    print "ok"
