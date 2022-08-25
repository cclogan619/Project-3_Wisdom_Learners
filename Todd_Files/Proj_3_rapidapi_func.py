import os
from pathlib import Path
import fire
import questionary
import requests
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
#%matplotlib inline
load_dotenv()

# Set Alpaca API key and secret by calling the os.getenv function and referencing the environment variable names
# Set each environment variable to a notebook variable of the same name
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

# Check the values were imported correctly by evaluating the type of each
print(type(alpaca_api_key))
print(type(alpaca_secret_key))

def option_chain_return(input_ticker, formatted_df):

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
   
    r = response.json()
    p = r["options"]

    df = pd.DataFrame(p)
    df = df.T
    formatted_df = df["Date"].dt.strftime("%m/%d/%y")
    formatted_df = formatted_df.set_index("Date")
    formatted_df = formatted_df.index()
    return formatted_df

def run():
    option_chain_return(input_ticker="CCL", formatted_df="r")
    return formatted_df 

if __name__ == "__main__":
    fire.Fire(run)