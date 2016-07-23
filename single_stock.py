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


   ax = df.plot(title = "Stock Prices",figsize=(15,8),label="Stock Prices")
   r_mean = get_rolling_mean(df,window=window)
   r_mean.plot(ax = ax,label ="mean")
   upper,lower = bollinger_bands(df,window=window)
   upper.plot(ax=ax, label ="upper")
   lower.plot(ax=ax, label ="lower")
   plt.legend(loc="upper left")
   plt.show()

   return 

def test_run():
   """
   Get data and analysis a single stock.
   """
   symbol =["AAPL"]
   start_date ='2014-01-01'
   end_date ='2016-12-31'
   dates = pd.date_range(start_date,end_date)
   data = get_data(symbol,dates)

   plot(data["AAPL"],window=50)
   


if __name__ == "__main__":

    test_run()
