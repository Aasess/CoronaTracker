
Step1 : Development(CoronaProject + Demo for project dir)

We need to parse the data(text) from "https://www.worldometers.info/coronavirus/". For this I am using

BeautifulSoup library + Requests library. Requests allows us to make HTTP request to get infomation from 

website and after that we can parse the http result using BeautifulSoup.(Can also use Pandas using read.html_csv()

but this site doesn't allow to read table using Pandas.i.e Authentication error also BeautifulSoup is really

powerful for parsing compared to pandas).

	requirement:

	1:Install beautifulSoup along with lxml(which is parser.Can use any parser. It doesn't matter)
	
	2: Install requests

	3:Install django

	4:Create django project and apps and templates or you can download the file
	
	5: Run the server


note: "watch the project demo "
note: "bootstrap is used for creating the templates"	


Step2:Web Scraping: Storing above parsed data to csv file(coronacsv:masterbranch) 

	2.1: first Convert the data parsed using beautifulSoup to csv format.(Those who want to use can
 	use the dataset).For this I will be using Pandas.
	
	I will be working on TimeSeries Analysis considering different project. Those who want to work on 
	the same Development can do the following
		* In App -> views.py after line53 of coronatracker..... copy the modified code of"Parsingandtocsv.py
		 file from coronacsv directory"
		
			
Step3: TimeSeriesAnalysis
			 