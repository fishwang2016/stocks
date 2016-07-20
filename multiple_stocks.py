# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 18:52:55 2016

@author: Fish
"""



"""build a dataframe"""
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
    dfSPY = pd.read_csv('data/SPY.csv',index_col='Date', parse_dates = True,
                        usecols = ['Adj Close','Date'])
    #print dfSPY
                        
    dfSPY =dfSPY.rename(columns ={'Adj Close':'SPY'})
                        
    df1 = df1.join(dfSPY,how ='inner')
    """
    choose proper parameters on how can drop NaN
    http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.join.html    
    """
    # drop NaN rows
    #df1=df1.dropna()
    
    
    stocks = ['GOOG','IBM','AAPL']
    
    for stock in stocks:
        df = pd.read_csv('data/%s.csv' % stock, index_col="Date",usecols =['Date','Adj Close'],
                         na_values =['nan'])
        df = df.rename(columns={"Adj Close":stock})
        df1 = df1.join(df,how='left')

    print df1
    
if __name__ =='__main__':
    test_run()