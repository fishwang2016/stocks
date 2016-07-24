"""
To analysis a single stock

1)indicators of up and down trend.
2)Tell the selling and buying opportunity
3)Visualize data.
 - Bollinger Bands
 - Moving Average

"""

from utility_stock import get_data, plot_data
import pandas as pd
import matplotlib.pyplot as plt

def get_rolling_mean(df,window=20):

    return pd.rolling_mean(df,window=window)

def get_rolling_std(df,window=20):

    return pd.rolling_std(df,window=window)

def bollinger_bands(df,window =20):
    
    r_mean = get_rolling_mean(df,window)
    r_std = get_rolling_std(df,window)

    upper_band = r_mean + 2 * r_std

    lower_band = r_mean - 2 * r_std

    return upper_band,lower_band


def plot(df,window =20):
   plt.figure(211)
   ax = df['Adj Close'].plot(title = "Stock Prices",figsize=(8,6),label="Stock Prices")
   r_mean = get_rolling_mean(df['Adj Close'],window=window)
   r_mean.plot(ax = ax,label ="mean")
   upper,lower = bollinger_bands(df['Adj Close'],window=window)
   upper.plot(ax=ax, label ="upper")
   lower.plot(ax=ax, label ="lower")
   plt.legend(loc="upper left")
   
   plt.figure(212)
   
   (df['Volume']/100000000).plot(kind ='bar',figsize=(8,2),use_index= False)
   plt.show()

   return 
   
def read_stock(symbol,dates):
    
    df1 = pd.DataFrame(index = dates)
    
    df = pd.read_csv('data/%s.csv' % symbol[0],usecols=['Date','Adj Close','Volume'],
                     
                     index_col ='Date',na_values='NaN')
                     
    df1 = df1.join(df,how ='inner')
    
    
    return df1.sort_index() 

def test_run():
   """
   Get data and analysis a single stock.
   """
   symbol =["AAPL"]
   start_date ='2014-01-01'
   end_date ='2016-12-31'
   dates = pd.date_range(start_date,end_date)
   data = read_stock(symbol,dates)

   plot(data,window=50)
   


if __name__ == "__main__":

    test_run()
