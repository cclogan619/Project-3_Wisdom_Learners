import streamlit as st
import pandas as pd
import sqlalchemy

st.title('Financial Dashboard')

engine = sqlalchemy.create_engine('sqlite:///fundamentals.db')

df = pd.read_sql('fundamentals', engine, index_col=['symbol'])

drop_down_I = st.selectbox('Choose a sector',
                            df.sector.unique())

drop_down_II = st.selectbox('Choose a metric',
                            df.columns[df.columns != 'sector'])

values = df[df.sector == drop_down_I][drop_down_II]

st.bar_chart(values)