# -*- coding: utf-8 -*-
import requests
import xmltodict
from bs4 import BeautifulSoup
from datetime import datetime

domain = 'https://www.glenat.com'
url = 'https://www.glenat.com/manga/a-paraitre'
res = []
while True:
    data = requests.get(url)
    html = BeautifulSoup(data.text, 'html.parser')
    timeline = html.select("#block-views-facettes-block-4 > div > div > div.view-content > div.views-row")
    # timeline = html.select('div.container div.row div.content > div.view > div.view-content > div.views-row')
    print(timeline)
    for item in timeline:
        # for string in item.stripped_strings:
        #     print(string)
        var = {'name': item.find('div', 'field-type-text').find('a').string,
               'date': datetime.strptime(item.find('div', 'field-type-datetime').string, '%d.%m.%Y'),
               'link': domain + item.find('div', 'field-type-text').find('a').attrs['href'],
               'author': item.find('ul').a.string
               }
        res.append(var)
    nextpage = html.select("#block-views-facettes-block-4 > div > div > table > tbody > tr > td.pagerer.pagerer-center > div > div > ul > li.pager-next.active > a")
    if nextpage:
        nextpage = nextpage[0].attrs['href']
        url = domain + nextpage
    else:
        break
for item in res:
    print("%s\n" % item)
