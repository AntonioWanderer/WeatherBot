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
		cell = soup
		items = cell.find_all('a')
		print("Done")
		for item in items:
			try:
				countries_links.append(item.get('href'))			
				countries.append(item.get_text())
			except:
				print("An exception, not tag, we need")
	else:
		print('Error') 
	return(countries, countries_links)
	
def parseFinal(addr):
	html = getHtml(addr)
	if html.status_code == 200:
		soup = bsp(html.text, 'html.parser') 
		currentTemp = soup.find('div', class_ = "ArchiveTemp").find('span').get_text()
		return currentTemp
