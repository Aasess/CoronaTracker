from django.shortcuts import render,redirect
from bs4 import BeautifulSoup
import requests
import json

def returnresult():
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
    return (datamodified)


def jsonresult(countryname):
    url = 'https://res.cloudinary.com/geotargetly/raw/upload/v1579830286/data/iso_3166_country_codes.json'
    
    #load the site
    data_source = requests.get(url)

    #convert the json file into python object
    data = data_source.json()

    for item in data:
        if(countryname == item["country_name"] or countryname == item["alpha_3"]):
            return item["alpha_2"]
        else:
            return countryname[:2]



# Create your views here.
def corona(request):
    datamodified = returnresult()
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
    CountrySearch = CountrySearch.upper()

    # calling the function
    datamodified = returnresult()
    # preparing the table
    finallist = []
    error = True

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
            error = False
        

    firsttwoletter = jsonresult(countryname)

    # dict
    context = {
        "countryname": countryname,
        "totalcase": totalcase,
        "recoveredcase": recoveredcase,
        "deathcases": deathcases,
        "activecases": activecases,
        "firstwo": firsttwoletter.lower()
    }
    return render(request, "coronaapp\countrywise.html", context)

