import os
import requests
from bs4 import BeautifulSoup as bsp

#URL parts to creating different url-s
URL0 = 'https://rp5.ru/Погода_в_мире'
URLi = ''
URL1 = ''
URL = URL0

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
           'accept': '*/*'}

def getHtml(url, params=None):
    r = requests.get(url, headers = HEADERS, params = params)
    return(r)

def getContent(html):
    soup = bsp(html, 'html.parser') 
    items = soup.find_all('div', class_ = 'country_map_links') 
    countries = []
    countries_links = []
    for item in items:
        if item.find('a') != None: 
            countries.append(item.find('a').get_text())
            countries_links.append(item.find('a').get('href'))
    return(countries, countries_links)

def parse(addr):
    html = getHtml(addr)
    if html.status_code == 200:
        data = getContent(html.text) 
    else:
        print('Error') 
    return(data)

countries_list, countries_links = parse(URL) 
print(countries_links)
