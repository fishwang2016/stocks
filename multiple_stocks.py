# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 18:52:55 2016

@author: Fish
"""



"""build a dataframe"""
stocks = ['GOOG','JD','IBM','SPY','AAPL']
import pandas as pd

def test_run():
    start_date ='2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date,end_date)
    #print dates[0]
    # Crate an empty dataframe
    df1 = pd.DataFrame(index = dates)
   # print df1
    
    #Read SPY data into temporary dataframe
    dfSPY = pd.read_csv('data/spy.csv')
    print dfSPY
    df1 = df1.join(dfSPY)
    print df1
    
if __name__ =='__main__':
    test_run()