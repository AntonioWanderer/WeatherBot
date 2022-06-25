import GetWeather as prs

URL0 = 'https://rp5.ru'
URL1 = '/Погода_в_мире'
URL = URL0 + URL1

countries_list, countries_links = prs.parse(URL) 
print(countries_links)
