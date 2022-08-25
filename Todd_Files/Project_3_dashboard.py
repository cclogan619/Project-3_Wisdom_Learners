import streamlit as st
import pandas as pd
import sqlalchemy
import yfinance as yf


st.title('Financial Dashboard')

engine = sqlalchemy.create_engine('sqlite:///fundamentals.db')

df = pd.read_sql('fundamentals', engine, index_col=['symbol'])

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

#API call from rapidapi.com for CCL
import requests


id = input_ticker
url = "https://option-chain.p.rapidapi.com/options/%s" % id 
print(url)
headers = {
	"X-RapidAPI-Key": "e17dcce559msh919faee0afa4c7bp1ce1a6jsn70cc4d9ff538",
	"X-RapidAPI-Host": "option-chain.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
r = response.json()
#p = r["options"][0]
"""
THIS SECTION PULLS THE EXPIRATION DATES FROM THE JSON FILE, TURNS THEM INTO A DATAFRAME AND TRANSPOSES
THE DATA FOR STREAMLIT TO PRESENT AS CHOICES IN A DROP DOWN MENU
"""

r = response.json()
p = r["options"]

df = pd.DataFrame(p)
df = df.T
df



st.write(df)


drop_down_III = st.selectbox('Choose an expiration date',
                            df.index)

q = r["options"][0][drop_down_III]



df2 = pd.DataFrame(q)

st.write(df2)

drop_down_IV = st.selectbox('Choose a call or put',
                            df2)

df3 = pd.DataFrame(drop_down_IV)

st.write(df3)
"""
r = response.json()
p = r["options"][0]['2022-08-26']['calls']
#convert python dictionary to dataframe
#Chain = pd.DataFrame.from_dict(r, orient = "index", columns=['date','strike', 'symbol', 'last'])
#Chain.head()
df = pd.DataFrame(p)
df
"""