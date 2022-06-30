import os
import requests
from bs4 import BeautifulSoup as bsp

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
           'accept': '*/*'}

def getHtml(url, params=None):
	r = requests.get(url, headers = HEADERS, params = params)
	return(r)

def parse(addr):
	html = getHtml(addr)
	if html.status_code == 200:
		soup = bsp(html.text, 'html.parser') 
		countries = []
		countries_links = []
		cell = soup.find('div', class_ = 'countryMap') 
		items = cell.find_all('a')
		for item in items:
    			countries_links.append(item.get('href'))			
    			countries.append(item.get_text())
	else:
        	print('Error') 
	return(countries, countries_links)

