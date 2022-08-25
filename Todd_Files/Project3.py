import pandas as pd
import numpy as np
import csv
from pathlib import Path
import MATLAB

df = pd.read_csv(Path("./CSV/Aug_19.csv"),
            index_col="Last Trade Date"    
)
print(df)

"""
Build in a function that calculates the value of the option contract from the data given:

Columns of data for Calls and Puts pulled/scraped from https://finance.yahoo.com/quote/CCL?p=CCL corresponding to the same expiration date.  This one is for August 19, 2022.  


Last Trade Date
Contract Name
Strike 
Last Price
Bid
Ask
Volume
Open Interest
Implied Volatility

# Black-Scholes model - options pricing model
NOTE: The Black-Scholes-Merton (BSM) prices European options.  These options do not trade except on the expiration date.
American options can be bought and sold at any date between issuance and expiration.  The model derived by Bjerksund-Stensland takes into account 
a number of items that the BSM model does not.  These are:

Source: Investopedia
The Bjerksund-Stensland model was developed in 1993 by Norwegians Petter Bjerksund and Gunnar Stensland and is used by investors 
to generate an estimate for the best time to execute an American option—financial derivatives that give buyers the right, but not 
the obligation, to buy (calls) or sell (puts) an underlying asset at an agreed-upon price and date.

The model is used specifically to determine the American call value at early exercise when the price of the underlying asset 
reaches a flat boundary and works for American options that have a continuous dividend, constant dividend yield, and discrete 
dividends. Bjerksund-Stensland divides the time to maturity into two periods with flat exercise boundaries — one flat boundary 
for each of the two periods.

American options differ from European options in that they can be exercised at any point during the contract period, rather 
than only on the expiration date. This feature should make the premium on an American option greater than the premium on a 
European option since the party selling the option is exposed to the risk of the option being exercised over the entire 
duration of the contract.

The Bjerksund-Stensland model takes into account that options may be exercised before the expiration date, while the 
popular Black Scholes Method does not. This means the latter isn't really suitable for calculating the price of 
American options and works best when pricing more straightforward European options.

That equation is: 



"""