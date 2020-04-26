from bs4 import BeautifulSoup
import requests
import pandas as pd

source = requests.get("https://www.worldometers.info/coronavirus/").text
soup = BeautifulSoup(source, 'lxml')

# fetching the table from the site with the power of soup
table = soup.find('table')
table_rows = table.find_all('tr')

data = []  # empty list

for item in table_rows:
    td = item.find_all('td')
    eachrow = [i.text for i in td]
    data.append(eachrow)

# cleaning(slicing) the data
datamodified = data[8:-8]

# sorting the data by country name
datamodified.sort()

# preparing the table
finallist = []
for row in datamodified:
    if (row[0] != "World"):
        datadict = {
            'Country': row[0],
            'TotalCases': row[1],
            'TotalDeath': row[3],
            'TotalRecovered': row[5],
            'ActiveCases': row[6],
        }
    # storing again in list or tuple format for passing with render request
    finallist.append(datadict)

# print(finallist[0]["Country"])
# print(finallist[1])

# converting list to each seires and then combining them to dataframe
series1 = []
series2 = []
series3 = []
series4 = []
series5 = []
for row in finallist:
    series1.append(row["Country"])
    series2.append(row["TotalCases"])
    series3.append(row["TotalDeath"])
    series4.append(row["TotalRecovered"])
    series5.append(row["ActiveCases"])

# we have obtained result in series
# converting the series to dataframe as:
df = pd.DataFrame({
    'Country': series1,
    'TotalCases': series2,
    'TotalDeath': series3,
    'TotalRecovered': series4,
    'ActiveCases': series5,
})
print(df.head(5))

df.to_csv("corona.csv", index = False)