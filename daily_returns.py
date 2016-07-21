# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 19:32:41 2016

@author: Fish
"""

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

from utility_stock import get_data ,plot_data,get_daily_returns

def test_run():
    
    symbols =['IBM','GOOG','AAPL']
    
    start_date = '2015-01-01'
    end_date = '2016-12-31'
    
    dates = pd.date_range(start_date, end_date)
    df =  get_data(symbols,dates)
    
    daily_returns= get_daily_returns(df)
    
    daily_returns['SPY'].hist(bins=20,figsize=(15,5),label='SPY')
    daily_returns['IBM'].hist(bins=20,label='IBM')
    plt.legend(loc="upper left")
    
    mean = daily_returns['SPY'].mean()
    print "Mean: ",mean
    std = daily_returns['SPY'].std()
    print "Std: ", std
    
    print daily_returns['SPY'].kurtosis()
    
    print daily_returns.corr(method='pearson')
    
    plt.axvline(mean,color='w',linestyle='dashed',linewidth=2)
    plt.axvline(std,color ='r',linestyle='dashed',linewidth=2)
    plt.axvline(-std,color ='r',linestyle='dashed',linewidth=2)
    
    
    daily_returns.plot(kind='scatter',x='SPY',y='IBM',figsize=(15,5))   
    
    # y = ax+ b
    
    beta_IBM , alpha_IBM = np.polyfit(daily_returns['SPY'],daily_returns['IBM'],1)
    plt.plot(daily_returns['SPY'],beta_IBM*daily_returns['SPY']+alpha_IBM,'-',color='r')
    
    plt.show()

   
    
    #plot_data(daily_returns['SPY'])

if __name__=='__main__':
    
    test_run()