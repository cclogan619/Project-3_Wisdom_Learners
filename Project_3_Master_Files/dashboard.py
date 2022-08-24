import streamlit as st
import pandas as pd
import yfinance as yf

st.title('Financial Dashboard')



df = pd.read_csv('Project_3_Master_Files/fundamentals.csv', index_col=['symbol'])

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
