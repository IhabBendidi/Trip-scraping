#Import Libraries
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup

headers = {
	'User-agent': 'harmless, for learning purposes so dont mind me poking',
	'From' : 'bendidiihab@gmail.com'
}

# specify the url
quote_page = 'https://www.majesticmorocco.com'

# query the website and return the html to the variable 'page'
page = requests.get(quote_page, headers = headers)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page.text, 'html.parser')

# Create a file to write to
f = csv.writer(open('Current Possible Travels.csv','a'))

# Take out the <x> of my desired data and get its value
type_box = soup.find_all('span' , attrs={'class' : 'label-warning'})
price_box = soup.find_all('span', attrs={'class' : 'price'})
startPlace_box = soup.find_all('div', attrs={'class' : 'val'})
circuit_box = soup.find_all('h4')

if type_box == [] or price_box == [] or startPlace_box == [] or circuit_box == [] :
	print("failure")
else:
	print("success")
	f.writerow(['Ville de depart', 'Circuit planifie', 'Type de voyage', 'prix du voyage'])


for i in range (len(type_box)) : 
	type = type_box[i]
	price = price_box[i]
	startPlace = startPlace_box[i]
	circuit = circuit_box[i]
	f.writerow([startPlace.text.strip(), circuit.text, type.text, price.text])


