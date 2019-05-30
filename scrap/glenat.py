# -*- coding: utf-8 -*-
from scrap.interface import InterfaceScrap
from datetime import datetime


class Glenat(InterfaceScrap):
    domain = 'https://www.glenat.com'
    url = domain + '/manga/a-paraitre'
    res = []

    def get_items(self):
        return self.html.select("#block-views-facettes-block-4 > div > div > div.view-content > div.views-row")

    def add_item(self, item):
        var = {'name': item.find('div', 'field-type-text').find('a').string,
               'date': datetime.strptime(item.find('div', 'field-type-datetime').string, '%d.%m.%Y').strftime('%d/%m/%Y'),
               'link': self.domain + item.find('div', 'field-type-text').find('a').attrs['href'],
               'editor': 'glénat',
               'author': item.find('ul').a.string
               }
        self.res.append(var)

    def get_next_page(self):
        return self.html.select(
            "#block-views-facettes-block-4 > div > div > table > tbody > tr > td.pagerer.pagerer-center > div > div > ul > li.pager-next.active > a")
