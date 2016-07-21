# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 19:32:41 2016

@author: Fish
"""

import pandas as pd

import matplotlib.pyplot as plt

from utility_stock import get_data ,plot_data,get_daily_returns

def test_run():
    
    symbols =["GOOG",'IBM','AAPL']
    
    start_date = '2015-01-01'
    end_date = '2016-12-31'
    
    dates = pd.date_range(start_date, end_date)
    df =  get_data(symbols,dates)
    
    daily_returns= get_daily_returns(df)
    
    daily_returns['SPY'].hist(bins=50,figsize=(15,5))
   
    
    #plot_data(daily_returns['SPY'])

if __name__=='__main__':
    
    test_run()