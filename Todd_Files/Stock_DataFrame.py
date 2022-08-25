# Import the required libraries and dependencies
import os
import requests
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
#%matplotlib inline

# Load the environment variables by calling the load_dotenv function
load_dotenv()

# Set Alpaca API key and secret by calling the os.getenv function and referencing the environment variable names
# Set each environment variable to a notebook variable of the same name
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

# Check the values were imported correctly by evaluating the type of each
(type(alpaca_api_key))
(type(alpaca_secret_key))

alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2")

"""
NOTE TO P3-G1: IF WE COULD SET THE DROP DOWN OR SET UP QUESTIONARY
TO ASK FOR A TICKER, WE CAN POPULATE THIS PART OF THE PROGRAM
IN REAL TIME.  THIS WILL ALSO DEPEND ON WHETHER WE CAN PULL IN
OPTIONS DATA IN REAL TIME.  FOR NOW, I'LL LEAVE THEM SET AS 
CONSTANTS AND NOT VARIABLES.
"""
# Set the tickers
tickers = ["CCL", "^GSPC", "INX", "$SPX"]

tickers

"""
NOTE SAME THOUGHT ON THE DATE RANGE TO CREATE THE STOCK/INDEX
DATAFRAME. FOR NOW, THE DATAFRAME IS 7 YEARS AND 2 MONTHS.
"""
start_date = pd.Timestamp("2015-06-15", tz="America/New_York").isoformat()
end_date = pd.Timestamp("2022-08-15", tz="America/New_York").isoformat()

timeframe = "1Day"

# Call to Alpaca to get the data requested: tickers, timeframe, start and end date.

portfolio_prices_df = alpaca.get_bars(
    tickers,
    timeframe,
    start = start_date,
    end = end_date
).df

portfolio_prices_df.head()



