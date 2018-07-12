#Import Libraries
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup


headers = {
	'User-agent': 'Trip Planner',
	'From' : 'bendidiihab@gmail.com'
}


# Create a file to write to
f = csv.writer(open('Travel Data.csv','a'))


# specify the url
quote_pages = ['https://www.majesticmorocco.com/excursions', 'https://www.majesticmorocco.com/voyages-organises']

for quote in quote_pages :
	page = requests.get(quote, headers = headers)
	print('Sucess retrieving pagination from' + quote)

	# parse the html using beautiful soup and store in variable 'soup'
	soup = BeautifulSoup(page.text, 'html.parser')


	pagination = soup.find('ul' , attrs={'class' : 'pagination'})
	if pagination :
		last_page = int(pagination.find_all('a')[-2].text)
	else :
		last_page = 1


	# here
	for i in range(1, last_page + 1):
		final_url = quote + '?page=' + str(i)

		page = requests.get(final_url, headers = headers)
		print('Success retrieving data from : ' + final_url)

		# parse the html using beautiful soup and store in variable 'soup'
		soup = BeautifulSoup(page.text, 'html.parser')
		if (quote == 'https://www.majesticmorocco.com/voyages-organises'):
			articles = soup.find_all('article', attrs={'class' : 'article'})
			for article in articles :
				type = 'Voyage Organisé'
				price = article.find('span', attrs={'class' : 'price'}).text.split('de')[-1].split('M')[0].strip()
				temp = article.find('h4')
				sejour_box = temp.text.split(':')[-1].strip().split('/')
				sejour = sejour_box[0].strip()  + ' & ' + sejour_box[1].strip()
				destination = temp.text.split('Validit')[0].strip()
				time = article.find('div', attrs={'class' : 'time'})
				periode = time.find('span', attrs={'style' : 'color: gray; font-style: italic;'}).text.strip()
				depart = time.find_all('div',  attrs={'class' : 'col-xs-6'})[1].text.split('Départ')[-1].strip()
				f.writerow([type, price, sejour, depart, destination, periode])
		elif quote == 'https://www.majesticmorocco.com/excursions':
			items = soup.find_all('div', attrs={'class' : 'item'})
			for item in items :
				type = 'Excursion'
				sejour = '1 Jours'
				periode = 'Sur demande'
				price = item.find('div', attrs={'class' : 'price'}).find('span').text.split('M')[0].strip()
				depart = item.find('div', attrs={'class' : 'location'}).text.strip()
				destination = item.find('div', attrs={'class' : 'content'}).find('h4').text.strip()
				f.writerow([type, price, sejour, depart, destination, periode])

