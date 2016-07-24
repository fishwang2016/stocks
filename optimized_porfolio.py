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

    S = E(Rp - Rr )/THETAp
    S: Sharp ratio
    rp: return of the portfolio
    rf: risk-free rate
    THETAp: standard deviation of returns of the portfolio 
   
"""
from utility_stock import get_data,plot_data,get_daily_returns
import pandas as pd
import matplotlib.pyplot as plt
import math 

def sharp_ratio(returns,rf =0.03):
    """
    SR can vary widely depending on how
    frequently you sample
    - SR is an annual measurement
    - SRannualized  = K * SR
    - K = sqrt(#samples per year)
    - daily K = sqrt(252)
    - weekly K = sqrt(52)
    - monthly k = sqrt(12)

    """
    daily_rf = math.pow(rf+1,1.0/252.0)-1
    std = returns.std()
    mean = (returns-daily_rf).mean()
    SR = mean/std
    
    return SR 

def daily_portfolio_value(data , weight,start_value):
    #normalized price
    norm = data/data.iloc[0]
    #alloced
    alloced = norm * weight
    #sum
    port = alloced.sum(axis=1)
    port_value = port * start_value
    return port_value

def statistics(port_val):
    cum_ret = port_val[-1]/port_val[0] -1
    print "Accumalitive Returns: ", cum_ret
    daily_rets = get_daily_returns(port_val)
 
    avg_daily_ret = daily_rets.mean()
    print "Average Daily Returns: ",avg_daily_ret
    std_daily_ret = daily_rets.std()
    print "Average Daily Returns Std: ", std_daily_ret
    print "Sharp Ratio: ",sharp_ratio(daily_rets)
    
    return 
def test_run():
    start_value = 100000
    weight =[1.2,0.5,0.3]
    if sum(weight)> 1:
        print "Weight sums bigger than 1. Please check."
        return
    symbols = ["IBM","GOOG","AAPL"]
    start_date ='2015-01-01'
    end_date ='2015-12-31'
    dates = pd.date_range(start_date, end_date)
    data = get_data(symbols, dates)
    #print data
    #print data.iloc[0]
    #daily = get_daily_returns(data)
    #print "symbols ",symbols
    #print data[symbols]
    #print "end symbols"
    #print p_daily
    d_port = daily_portfolio_value(data[["IBM","AAPL","GOOG"]],weight,start_value)
    statistics(d_port)
    d_port.plot(title = 'Daily Portfolio Value',figsize=(15,5),label ="Portfolio Value")
    plt.legend(loc ='upper left')
    plt.show()
if __name__ == '__main__':

    test_run()
