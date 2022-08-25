import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime
from prophet import Prophet
from prophet.plot import plot_plotly
import numpy as np

st.title('Financial Dashboard')


# Use this for working on streamlit
df = pd.read_csv('Project_3_Master_Files/fundamentals.csv', index_col=['symbol'])

# Use this for working on localhost
# df = pd.read_csv('fundamentals.csv', index_col=['symbol'])

drop_down_I = st.selectbox('Choose a sector',
                            df.sector.unique())

drop_down_II = st.selectbox('Choose a metric',
                            df.columns[df.columns != 'sector'])

values = df[df.sector == drop_down_I][drop_down_II]

st.bar_chart(values)

st.header('Company Information')
input_ticker = st.text_input('Enter a stock symbol (all caps please)')
st.write(input_ticker)
x = yf.Ticker(input_ticker).history(period='max')
st.write(x.describe())
# st.write(x)
close_df = x[['Close']].copy()
st.line_chart(close_df)


forcast_df = close_df.reset_index()
forcast_df.columns = ['ds', 'y']
forcast_df = forcast_df.dropna()
st.write(forcast_df.head())
st.write(forcast_df.tail())

m = Prophet()
m.fit(forcast_df)
future = m.make_future_dataframe(periods=8760, freq='H')
forcast = m.predict(future)
st.subheader('Forcast Data')
st.write(forcast.tail())

st.title('Forcast - Facebook Prophet')
st.write('forcast data')
fig1 = plot_plotly(m, forcast)
st.plotly_chart(fig1)

st.write('forcast components')
fig2 = m.plot_components(forcast)
st.write(fig2)

st.write("Learn More about Options [http://github.com/cclogan619/Project-3_Wisdom_Learners/Catherine_Files/Robinhood_Options_Training.pdf](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")