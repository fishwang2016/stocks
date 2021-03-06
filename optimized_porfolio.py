"""

This is to generate a optimized portfolio

Input:  Data, Ratio
Output: Data , Optimized_Ratio

Parameters: 

Data - input  stocks data ( prices of portfolio stocks )
Ration - weighting of different stocks.

How to evaluate portfolio performance:
    1) Returns
    2) Risk

    Target: high returns with low risk
    Sharp Ratio :

    S = (Rp - Rr )/THETAp
    S: Sharp ratio
    rp: return of the portfolio
    rf: risk-free rate
    THETAp: standard deviation of returns of the portfolio 
   
"""
from utility_stock import get_data,plot_data,get_daily_returns
import pandas as pd
import matplotlib.pyplot as plt
import math 

def sharp_ratio(returns,rr =0.03):
    rr = math.pow(rr,1.0/252.0)
    rp = returns.sum()
    std = returns.std()
    
    return (rp -rr)/std

def normalized_prices(data):
    """
    Normalized all the stock prices

    Example: 

    The first data , and each date is related to the first data[0]

    """
    return data/data.iloc[0]


def portfolio_returns(data,weight):
    # daily returns for each stock
    daily = get_daily_returns(data)
    
   # print "data"
   # print daily
   # print "_________"
    p_daily = daily * weight
       
    p_daily["sum"] = p_daily.sum(axis = 1)    
    
    #print p_daily
    return p_daily 


def test_run():
    weight =[0.0,0.5,0.3]
    symbols = ["IBM","GOOG","AAPL"]
    start_date ='2015-01-01'
    end_date ='2015-12-31'
    dates = pd.date_range(start_date, end_date)
    data = get_data(symbols, dates)
    #print data
    data = normalized_prices(data)
    #print data.iloc[0]
    #daily = get_daily_returns(data)
    #print "symbols ",symbols
    #print data[symbols]
    #print "end symbols"
    p_daily = portfolio_returns(data[["IBM","GOOG","AAPL"]],weight)
    #print p_daily
    print sharp_ratio(p_daily["sum"])
    data.plot(title = 'Normalized Price',figsize=(15,5))
    plt.legend(loc ='upper left')
    plt.show()
if __name__ == '__main__':

    test_run()
