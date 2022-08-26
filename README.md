
# *FinTech Boot Camp Project 3 Repository - README.md File*
# Catherine Logan, Richard Kell, Todd Garner
---


# Stock and Options analysis - Python/Streamlit/AWS

This project started as an options pricing project using one stock and CSV's to pull tabular data from various sources like Yahoo! Finance, ALPACA and it has morphed into something different, mostly due to time available to each participant and our relative inexperience with the "hard core" Python and its libraries' functionality and syntax.  We intended to have a "bot" occupy the live program available for and asking questions of the User.  Additionally, we decided to utilize Streamlit (a Web3 interface that presented results to a browser, rather than in a .py program or Jupyter Notebook.  

We've largely had success in employing Streamlit, although we believe it was the culprit in the failure of parsing the dictionary/list data that was supplied via API from rapidapi.com.  In short, what functioned perfectly in a stand alone Python environment, failed miserably in the Streamlit environment.  

At one point, we had a working model that would allow the User to enger any valid Ticker symbol and populate a table with broad descriptions of the selected stock.  Additionally, a line chart was posted of that particular stock.  The selected Ticker symbol would then automatically populate an API call for the aforementioned deeply nested dictionary/list.  Considerable time was spent converting various elements in the parsed data to the appropriate data type (string, int, float, etc.).  However, using particular functions proved impossible when applying certain math formulas to a DataFrame in the Streamlit environment.  The Black Scholes Merton model was constructed and all variables formulated and populated with good data.  It was in the construction of the final equation in a DataFrame environment that proved to be this effort's undoing.  

In Streamlit, SQL databases were called and successfully deployed along with drop down menus for various selections by the User who would then enjoy bar charts and line graphs.  The selection offered to the User to pick a valid Ticker works famously and populates further functionality, albeit undeployed.  Below, you'll see a screenshot of the presentation initiatially seen by the User, including the first drop-down menu.  

![Stream_lit](Initial_streamlit_screen.png)

The upper section is composed of sector analyses and then specific metrics related to that sector.  As seen below, the lower drop down is a selection of metrics and then the bar chart results.

![Second_drop_down](Second_drop_down.png)

And, the results:

![Sector_metrics_results](sector_metrics_results.png)

The next section below turns from sector specific to company specific.  A User can input any valid Ticker and see the analysis of the .describe() attribute for the stock DataFrame as well as the latest line graph of the selected stock.  A text box allows the User to choose which company to review, as seen below.

![Company_info_ticker](Company_info_ticker.png)

The next section employs Facebook's Prophet application.  






The section below that is where all of the option data magic was supposed to occur.  What we ended up with was three options chains for CCL (Carnival Cruise Lines) with a drop down menu giving the User the ability to choose between 3 different expiration dates.  An options chain corresponding to these expiration dates is then posted.  These are pulled from CSV files from screen scrapes only.  No functionality from an API was demystified and resolved, as seen below.  

![Options_menu](options_menu.png)

![Options_chain](options_chain.png)

A link is provided for those that seek additional information about options and options strategies. 

---

## Technologies

This project was written in Python code, debugged in VS Code, presented via Streamlit and also employing Facebook Prophet.    

The Language can be found at [Python](<http://python.org>) and the VS Code can be found at [VS_Code](https://code.visualstudio.com/). The Streamlit application is used and can be found here [Streamlit](https://streamlit.io/).  

This particular program will run on Windows 10 via VS Code which launches Streamlit in a new browser.  

---

## Installation Guide

### Make sure all files are in the same directory. 
Utilizing VS Code, in the explorer window and the terminal below, navigate to the folder "Final_staging_folder."  From there, the User can launch this program by typing in the terminal (making sure that the terminal is navigated to the folder containing the program files) and type: 

*Streamlit run dashboard.py*  

From there, the new browser will launch and all functionality described above will be visible.  
```



## Contributors

Project 3 - Group 1: Catherine Logan, Richard Kell and Todd Garner.  All work was performed by our group members and uploaded to our central repository https://github.com/cclogan619/Project-3_Wisdom_Learners

There are several files for each team member that include the work done and uploaded. The Project 3 Master Files directory is where the dashboard.py program is located.  

---

## License

Anyone may use this program with proper references made in your work
