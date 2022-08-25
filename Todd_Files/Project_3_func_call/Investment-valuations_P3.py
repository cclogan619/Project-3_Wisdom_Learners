#API call from rapidapi.com for CCL
import requests
import os
import requests
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
#%matplotlib inline
import streamlit as st
from Project_3_functions import put_call

st.title('Options Chain')
st.header('Company Information')


input_ticker = st.text_input('Enter a stock symbol (all caps please)')
st.write(input_ticker)

df = put_call(input_ticker)
df1 = put_call(input_ticker)


st.header('Call Chain')
st.write(df)
st.header('Put Chain')
st.write(df1)