
def put_call(input_ticker):
    import pandas as pd
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
    p = r["options"][0]['2022-08-26']['calls']
    #p = r:options].[0].'2022-08-26'.calls

    df = pd.DataFrame(p)


    r = response.json()
    p = r["options"][0]['2022-08-26']['puts']
    #convert python dictionary to dataframe
    #Chain = pd.DataFrame.from_dict(r, orient = "index", columns=['date','strike', 'symbol', 'last'])
    #Chain.head()
    df1 = pd.DataFrame(p)

    return df, df1