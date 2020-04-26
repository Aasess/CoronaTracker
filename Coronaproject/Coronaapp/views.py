from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.
def corona(request):
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
        if (row[0] == "World"):
            worldtotalcase = row[1]
            worldrecoveredcase = row[5]
            worlddeathcases = row[3]
            worldactivecases = row[6]

    # dict
    context = {
        "corona": finallist,
        "worldtotalcase": worldtotalcase,
        "worldrecoveredcase": worldrecoveredcase,
        "worlddeathcases": worlddeathcases,
        "worldactivecases": worldactivecases,
    }
    return render(request, "Coronaapp\CoronaTracker.html", context)


def country(request):
    CountrySearch = request.GET['CountrySearch']
    #print(type(CountrySearch))
    CountrySearch = CountrySearch.upper()
    #print(CountrySearch)
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
        datadict = {
            'Country': row[0],
            'TotalCases': row[1],
            'TotalDeath': row[3],
            'TotalRecovered': row[5],
            'ActiveCases': row[6],
        }
        # storing again in list or tuple format for passing with render request
        finallist.append(datadict)

        if (row[0].upper() == CountrySearch):
            countryname = row[0]
            totalcase = row[1]
            recoveredcase = row[5]
            deathcases = row[3]
            activecases = row[6]

    firsttwoletter = countryname[:2].lower()
    #print(firsttwoletter)

    # dict
    context = {
        "countryname": countryname,
        "totalcase": totalcase,
        "recoveredcase": recoveredcase,
        "deathcases": deathcases,
        "activecases": activecases,
        "firstwo" : firsttwoletter
        }
    return render(request, "coronaapp\countrywise.html",context)