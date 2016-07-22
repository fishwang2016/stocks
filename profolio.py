"""
# Input some stocks and findout optimized profolio

Example:

stocks = ["GOOG","IBM",AAPL]
ratio  =[0.2,0.3,0.5]

output an optimized ration according to the history data

"""
import scipy.optimize as spo

import numpy as np

import matplotlib.pyplot as plt

def error(line,data):
    
    """
    Compute error between given line model and observed data
    
    Parameters
    --------------------
    line: tuple/list/array (C0, C1) where C0 is slope and C1 is Y-intercept
    data: 2D array where each row is a point(x,y)
    
    Returns error as a single real value.
    
    """
    
    err = np.sum((data[:,1]-line[0]*data[:,0]-line[1])**2)
    
    return err
    
def fit_line(data,error_func):
    
    """
    Fit a line to given data, using a supplied error function.
    
    
    Parameters:
    ------------------
    
    data: 2D array where each row is a point(X0, Y)
    
    """
    
    l= np.float32([0,1]) # slope =0 , intercept = mean(y values)
    
    #Plot initial guess (optional)
    x_ends = np.float32([-5,-5])
    
    plt.plot(x_ends, x_ends * l[0]+l[1])
    
    
    #Call optimizer to minimize error function
    
    result = spo.minimize(error_func,l,args=(data,),method ='SLSQP',options={'disp':True})
 
    print "result"
    print "------------------------"
    print result
    print "------------------------"
    
    return result.x

def f(x):
    
    y= (x-12)**2 +2*x +12
    
    print "x ={}, y = {}".format(x,y)


    return y 


def test_run():
    
    #Define original line
    
    l_orig = np.float32([4,2])
    print "Original line: C0 = {}, C1 = {}".format(l_orig[0],l_orig[1])
    Xorig = np.linspace(0,10,21)
    Yorig = l_orig[0]* Xorig + l_orig[1]
    plt.plot(Xorig, Yorig, 'b--',linewidth=2.0, label ='Original line')
    
    
    #Generate noisy data points
    
    noise_sigma =3.0
    noise = np.random.normal(0,noise_sigma, Yorig.shape)
    data = np.asarray([Xorig, Yorig+noise]).T
    plt.plot(data[:,0],data[:,1],'go',label='Data points')
    
    # Try to fit a line to this data
    
    l_fit = fit_line(data, error)
    print "Fitted line: C0 = {}, C1 = {}".format(l_fit[0],l_fit[1])
    plt.plot(data[:,0],l_fit[0] * data[:,0] + l_fit[1],'r--',linewidth =2.0,label ="Optimized")
    
    plt.legend(loc ='upper left')
#==============================================================================
#     Iguess =0
#      
#     mini_result = spo.minimize(f, Iguess,method='SLSQP',options={'disp':True})
#  
#     print "X = {}, y= {}".format(mini_result.x, mini_result.fun)
#     
#     xPlot = np.linspace(0,22,40)
#     yPlot = f(xPlot)
#     
#     plt.plot(mini_result.x,f(mini_result.x),'ro')
#     
#     plt.plot(mini_result.x,'r')
#     
#     plt.plot(xPlot,yPlot)
#==============================================================================
     
if __name__ == '__main__':
    
    test_run()

