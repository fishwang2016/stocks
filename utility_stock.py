# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 20:34:18 2016

@author: Fish
"""

"""utility functions"""

import os
import pandas as pd

import matplotlib.pyplot as plt

def rolling_bands():
    
    pass


def plot_selected(df,columns,start_date,end_date):
    #print df.ix[start_date:end_date,columns]
    
    
    
    plot_data(df.ix[start_date:end_date, columns])

def plot_data(df, title="Stock Prices",figsize=(15,5)):
    
    ax = df.plot(title=title,fontsize=10,figsize=figsize)
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
        
    return df.sort_index()
    
def get_rolling_mean(df, window=20):
    
    return pd.rolling_mean(df,window=window)
    
def get_rolling_std(df,window=20):
    
    return pd.rolling_std(df,window=window)
    
def get_bollinger_bands(rm,rstd):
    
    upper_band = rm + 2 * rstd
    lower_band = rm - 2 * rstd
    return upper_band, lower_band
def get_daily_returns(df):
    
    daily_returns = df.copy()
    
 # here comes .values
    
   # daily_returns[1:] = (daily_returns[1:]/daily_returns[:-1].values)-1
   
    
    #another way to do it is:
    daily_returns =(df/df.shift(1)) -1 # much easier with pandas
    
    daily_returns.ix[0] = 0
    
    
  
    return daily_returns
    
def test_run():
    
     symbols=['AAPL','GOOG','IBM']
     
     start_date = '2015-02-01'
     end_date ='2015-02-10'
     dates = pd.date_range(start_date,end_date)
     
     df = get_data(symbols,dates)
     # plot SPY data , retain matplotlib axis object
     ax = df['SPY'].plot(title = "SPY Rolling Mean",label ='SPY',figsize=(15,5))
     
     rm_SPY = pd.rolling_mean(df['SPY'],window =20)
     
     # Add rolling mean to same plot
     
     rm_SPY.plot(label="Rolling mean", ax=ax)
     ax.set_xlabel("Date")
     ax.set_ylabel("Price")
     
     rm = get_rolling_mean(df['SPY'])
     rstd = get_rolling_std(df['SPY'])
     
     upper_band , lower_band = get_bollinger_bands(rm, rstd)
     
     #demonistrate fillna
     upper_band.fillna(method='bfill',inplace = True)
     
     upper_band.plot(label="upper_band",ax=ax)
     lower_band.plot(label="lower_band",ax=ax)
     
     ax.legend(loc='upper left')
     
     plt.show()
     

     #daily = get_daily_return(df[['SPY','AAPL','GOOG']])

     daily = get_daily_returns(df['SPY'])

     
     daily.plot(title ="SPY Daily Returns",figsize=(15,5))
     
     plt.show()

#==============================================================================
#      # Slice by row range (dates) using DataFrame.ix[] selecgtor
#     # print df
#      print "-----------------------"
#      #dd = df['2015-01-01':'2015-01-31']
#      
#      df = df.sort_index()
#      print "Mean"
#      print df.mean()
#      print "Median"
#      print df.median()
#      print "Std"
#      print df.std()
#      
#      #df = df/df.ix[0]
#      
#      
#      
#      #plot_data(df)
#      plot_data(df/df.ix[0])
#     
#==============================================================================
  
    
if __name__ =='__main__':
    
     test_run()
    
    #test_run()
#==============================================================================
#      symbols=['AAPL','GOOG','IBM']
#      
#      start_date = '2010-01-01'
#      end_date ='2015-02-10'
#      dates = pd.date_range(start_date,end_date)
#      
#      df = get_data(symbols,dates)
#      # Slice by row range (dates) using DataFrame.ix[] selecgtor
#     # print df
#      print "-----------------------"
#      #dd = df['2015-01-01':'2015-01-31']
#      # sorting the data to ensure correct order while printing out
#      # and by sorting out will prevent empty data from slicing... 
#      df=df.sort_index()
#      
#      df = df/df.ix[0]
#      
#==============================================================================
     #plot_data(df)
    
    
     