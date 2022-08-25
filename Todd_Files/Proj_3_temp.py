    
import os
import requests
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import json 
#%matplotlib inline
load_dotenv()

# Set Alpaca API key and secret by calling the os.getenv function and referencing the environment variable names
# Set each environment variable to a notebook variable of the same name
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

# Check the values were imported correctly by evaluating the type of each
print(type(alpaca_api_key))
print(type(alpaca_secret_key))
Ticker = str("CCL")
CCL = Ticker
Ticker = CCL
id = str(Ticker)
url = "https://option-chain.p.rapidapi.com/options/%s" % id 
print(url)
headers = {
    "X-RapidAPI-Key": "e17dcce559msh919faee0afa4c7bp1ce1a6jsn70cc4d9ff538",
    "X-RapidAPI-Host": "option-chain.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
r = response.json()
#p = r["options"][0]


#r = response.json()
#p = r["options"]

#print(p)

options_dta = []

for i in r.items():

    options_dta.append([i[0], i[1]])

hh = pd.DataFrame(options_dta, columns = ['options', 'k'])

hh=hh.explode('k')

options_frame = pd.json_normalize(json.loads(hh.to_json(orient="records")))
options_frame





"""
df_prime = pd.DataFrame(np.arange(1.0, 5.0), index=index)
df_unstack = df_prime.unstack(level = 0)
df_unstack


df = pd.DataFrame(p)
df = df.T
df

formatted_df = df["date"].dt.strftime("%m/%d/%y")
formatted_df = formatted_df.set_index("date")
formatted_df = formatted_df.index()
formatted_df
"""