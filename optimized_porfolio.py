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

"""
from utility_stock import get_data,plot_data
import pandas as pd
import matplotlib.pyplot as plt
def normalized_prices(data):
    """
    Normalized all the stock prices

    Example: 

    The first data , and each date is related to the first data[0]

    """
    return data/data.iloc[0]

def test_run():
    weight =[0.2,0.5,0.3]
    symbols = ["IBM","GOOG","AAPL"]
    start_date ='2015-01-01'
    end_date ='2015-1-31'
    dates = pd.date_range(start_date, end_date)
    data = get_data(symbols, dates)
    #print data
    data = normalized_prices(data)
    #print data.iloc[0]
    data.plot(title = 'Normalized Price',figsize=(15,5))
    plt.legend(loc ='upper left')
    plt.show()
if __name__ == '__main__':

    test_run()
