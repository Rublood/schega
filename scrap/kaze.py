# -*- coding: utf-8 -*-
import requests
import xmltodict
from bs4 import BeautifulSoup
from datetime import datetime

domain = 'http://manga.kaze.fr'
url = 'http://manga.kaze.fr/planning'
res = []
while True:
    data = requests.get(url)
    html = BeautifulSoup(data.text, 'html.parser')
    timeline = html.select("#com_planning > div.mod_hikashop_listing.hikashop-cal-list div.hikashop_listing_item")
    if not timeline:
        break
    for item in timeline:
        var = {'name': item.find('h2', 'mangatitle').find('span').string + item.find('h2', 'mangatitle').find_all('span')[1].string,
               'date': datetime.strptime(item.find('span', 'manga_date').string, '%d/%m/%y'),
               'link': domain + item.find('a').attrs['href']
               }
        res.append(var)
    nextpage = html.select("#com_planning > div.navigation > a.next")
    if nextpage:
        url = domain + nextpage[0].attrs['href']
    else:
        break
for item in res:
    print("%s\n" % item)
