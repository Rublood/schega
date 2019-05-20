# -*- coding: utf-8 -*-
import requests
import xmltodict
from bs4 import BeautifulSoup
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME,'')

domain = 'https://www.kana.fr'
url = 'https://www.kana.fr/wp-admin/admin-ajax.php?action=do_ajax&fn=ajax_get_planning&startDate=201905&nbMonth=12'
res = []
while True:
    data = requests.get(url)
    html = BeautifulSoup(data.text, 'html.parser')
    timeline = html.select("div.item.support_manga")
    if not timeline:
        break
    for item in timeline:
        var = {'name': (item.find('h3').a.string + item.find('div', 'sub').string),
               'date': datetime.strptime(item.find('div', 'date').string, '%d %B %Y'),
               'link': item.find('a').attrs['href']
               }
        res.append(var)
    nextpage = False
    if nextpage:
        url = domain + nextpage[0].attrs['href']
    else:
        break
for item in res:
    print("%s\n" % item)
