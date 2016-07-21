# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 20:34:18 2016

@author: Fish
"""

"""utility functions"""

import os
import pandas as pd

import matplotlib.pyplot as plt


def plot_selected(df,columns,start_date,end_date):
    #print df.ix[start_date:end_date,columns]
    
    
    
    plot_data(df.ix[start_date:end_date, columns])

def plot_data(df, title="Stock Prices",figsize=(15,5)):
    
    ax = df.plot(title=title, fontsize=2,figsize=figsize)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def symbol_to_path(symbol, base_dir="data"):
    """return csv file path given ticker symbol."""
    return os.path.join(base_dir,"{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """ Read stock data (adjusted close) for given symbols from CSV files. """
    
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0,'SPY')
        
    for symbol in symbols:
        
        df1 = pd.read_csv(symbol_to_path(symbol),usecols=['Date','Adj Close'],
                         index_col='Date',na_values =['nan'] )
        df1 = df1.rename(columns ={"Adj Close": symbol}) 
        #print df1
        df = df.join(df1,how='inner')
        
    return df
    
def test_run():
    
     symbols=['AAPL','GOOG','IBM']
     
     start_date = '2014-01-01'
     end_date ='2015-02-10'
     dates = pd.date_range(start_date,end_date)
     
     df = get_data(symbols,dates)
     # Slice by row range (dates) using DataFrame.ix[] selecgtor
    # print df
     print "-----------------------"
     #dd = df['2015-01-01':'2015-01-31']
     
     df = df/df.ix[-1]
     
     #plot_data(df)
     plot_selected(df,symbols,'2015-01-01','2015-02-05')
    
  
    
if __name__ =='__main__':
    
    #test_run()
     symbols=['AAPL','GOOG','IBM']
     
     start_date = '2014-01-01'
     end_date ='2015-02-10'
     dates = pd.date_range(start_date,end_date)
     
     df = get_data(symbols,dates)
     # Slice by row range (dates) using DataFrame.ix[] selecgtor
    # print df
     print "-----------------------"
     #dd = df['2015-01-01':'2015-01-31']
     # sorting the data to ensure correct order while printing out
     df=df.sort_index()
     
     df = df/df.ix[0]
     
     #plot_data(df)
     plot_selected(df,symbols,'2015-01-01','2015-02-05')
    
    
     