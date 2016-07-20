# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 20:34:18 2016

@author: Fish
"""

"""utility functions"""

import os
import pandas as pd

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
    
     symbols=['AAPL','GOOG']
     
     start_date = '2015-01-01'
     end_date ='2015-02-10'
     dates = pd.date_range(start_date,end_date)
     
     df = get_data(symbols,dates)
     print df
     df.plot()
    
if __name__ =='__main__':
    
    test_run()
    
     