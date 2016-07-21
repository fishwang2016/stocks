# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:18:47 2016

@author: Fish_user
"""

""" Creating Numpy arrays"""

import numpy as np

import time
#==============================================================================
# Documentation:
# time.time: Current time in seconds (float value)
# timeit: Average execution time measurement
# profile: Code profiling
# iPython "magics":
# %time: How long does it take to run once
# %timeit: Averaged over multiple runs
# %prun/%lprun: Per-function/line profiling
#==============================================================================
# checking the time running a function

def how_long(func,*args):
    """Execute function with given arguments"""
    
    t0 = time.time()
    
    result = func(*args) # all arguments are passed
    
    t1= time.time()
    
    return result , t1-t0

def get_max_index(a):
    return a.argmax()
    
    
def manual_mean(arr):
    """Manually compute mean of all elements"""
    sum = 0
    
    for i in xrange(0,arr.shape[0]):
        for j in xrange(0,arr.shape[1]):
            sum = sum+arr[i,j]
    return sum / arr.size

def numpy_mean(arr):
    return arr.mean()

def test_run():
    
    a = np.array([(1,2,3,4,5),(10,20,30,40,50)])
    
    b = np.array([(2,2,1,3,5),(2,10,1,6,8)])
    
    print "Original array a :\n",a
    
    # Multiply a by 2
    
    print "\n Multiply a by 2: \n",2*a
    
    # didvided by 2
    
    print "\nArray divided by 2:\n", a/2.0
    
    # multipy a and b
    print "\nArray a * b:\n", a*b
    
    
#==============================================================================
#     a = np.random.rand(5)
#     indices = np.array([1,1,2,3])
#     
#     print a 
#     print "------------------------------"
#     
#     print a[indices]
#     
#     # calculating mean
#     mean = a.mean()
#     print mean 
#     print "***************************"
#     
#     # masking 
#     print a[a< mean]
#     
#     
#==============================================================================
#==============================================================================
#     
#     nd1 = np.random.random((1000,10000))
#     
#     # time manual
#     
#     print how_long(manual_mean,nd1)
#     
#     print "-----------------------------"
#     print how_long(numpy_mean, nd1)
#     
#==============================================================================
    # time array
    
    # List to 1D array
#==============================================================================
#     print np.empty((2,1))
#     print np.array([2,3,4])
#     print np.ones((5,4))
#     print np.zeros((6,3))
#     # specifying the datatype
#     print np.ones((5,4),dtype = np.int_)
#==============================================================================
#==============================================================================
#      print np.random.rand(5,4)
#      print "**************************"
#      print np.random.random((12,2))
#      print "***********************"
#      print np.random.normal(12,0.5,size=(2,3)) # 2X3 array
#      print np.random.normal(12,0.5,size=5 )#5 integers
#==============================================================================

#==============================================================================
#       #data type
#       a = np.random.random((5,4)) # 5X4 array 
#       print a
#       print a.shape
#       print a.shape[0] # number of rows
#       print a.shape[1] # number of columns
#       print a.dtype
#       print a.size
# 
#==============================================================================

#==============================================================================
# # Mathematical functions
#        np.random.seed(2)
#        a = np.random.random((5,6))
#        print a
#        print a.sum()
#        print a.min()
#        print a.max()
#        print a.mean()
#        print get_max_index(a)
#  
#==============================================================================


if __name__=="__main__":
    test_run()

