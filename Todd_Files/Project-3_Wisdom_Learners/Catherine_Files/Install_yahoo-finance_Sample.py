#pip install yahoo-finance

import os
import numpy as np 
import pandas as pd 
import yfinance as yf
import requests
import alpaca_trade_api as tradeapi


# retrieving yahoo indices for cryptocurrency
crypto_indices = pd.read_html(requests.get('https://finance.yahoo.com/cryptocurrencies').text)
major_crypto = crypto_indices[0]
major_crypto.head()


#Collecting BTC-USD
btc_data = yf.Ticker('BTC-USD')

#Creating BTC history data for 2 months
btc_df = btc_data.history(period='2mo', start='2022-02-05', end='2022-05-05')

# View header and tail of BTC for 2 months
print("BTC-USD data frame from: April 20, 20220 - May 05, 2022")
print("-----------------------------------------------------")
display(btc_df.head())
display(btc_df.tail()

# BTC-USD data frame from: April 20, 20220 - May 05, 2022


# Dropping last 2 columns of BTC 
btc_new_df = btc_df.drop(columns=['Stock Splits','Dividends'], axis=1)
print("BTC-USD update:")
print("---------------")
btc_new_df

#csv BTC-USD file
btc_new_df.to_csv('BTC-USD.csv',float_format='%.2f') 

# retrieving ETH-USD ticker
eth_data = yf.Ticker('ETH-USD')

#Creating ETH history data for 2 months
eth_df = eth_data.history(period='2mo', start='2022-02-05', end='2022-05-05')

# View header and tail of ETH for 2 months
print("ETH-USD data frame from: April 20, 20220 - May 05, 2022")
print("-----------------------------------------------------")
display(eth_df.head())
display(eth_df.tail())

# Dropping last 2 columns of ETH 
eth_new_df = eth_df.drop(columns=['Stock Splits','Dividends'], axis=1)
print("ETH-USD update:")
print("---------------")
eth_new_df

# ETH-USD csv file
doge_new_df.to_csv('DOGE-USD.csv',float_format='%.2f')

# retreiving Index tickers
stock_indices = pd.read_html(requests.get('https://finance.yahoo.com/world-indices/').text)
major_Stock = stock_indices[0]
major_Stock.head()

#Collecting S&P500 indice
sp_data = yf.Ticker('^GSPC')

# sp500 date range
sp500_df = sp_data.history(period='2mo', start='2022-02-05', end='2022-05-05')

# viewing sp500 df
print("S&P500 data frame from: April 20, 20220 - May 05, 2022")
print("-----------------------------------------------------")
display(sp500_df.head())
display(sp500_df.tail())




