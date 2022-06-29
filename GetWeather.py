import os
import requests
from bs4 import BeautifulSoup as bsp

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

def parse(mode, addr):
    if mode == 1:
    	print("Parser starts")
    html = getHtml(addr)
    if html.status_code == 200:
        data = getContent(html.text) 
    else:
        print('Error') 
    return(data)

