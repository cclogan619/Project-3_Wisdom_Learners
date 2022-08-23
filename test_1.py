import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf
# from yahoofinancials import YahooFinancials

msft = yf.Ticker("MSFT")


hist = msft.history(period = '1y')
# df_msft_close = pd.DataFrame['Close']
st.write(type(hist))
st.write(hist.columns)
st.write(hist.head())
st.write(hist.index[0])
test_df = hist.drop(hist.columns[[0, 1, 2, 4, 5, 6]], axis = 1)
st.write(test_df.head())

# df2 = df.drop(df.columns[[0, 1, 2]],axis = 1)