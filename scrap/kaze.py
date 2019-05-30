# -*- coding: utf-8 -*-
from datetime import datetime
from scrap.interface import InterfaceScrap


class Kaze(InterfaceScrap):
    domain = 'http://manga.kaze.fr'
    url = domain + '/planning'

    def get_items(self):
        return self.html.select("#com_planning > div.mod_hikashop_listing.hikashop-cal-list div.hikashop_listing_item")

    def add_item(self, item):
        var = {
            'name': item.find('h2', 'mangatitle').find('span').string + item.find('h2', 'mangatitle').find_all('span')[
                1].string,
            'date': datetime.strptime(item.find('span', 'manga_date').string, '%d/%m/%y').strftime('%d/%m/%Y'),
            'link': self.domain + item.find('a').attrs['href'],
            'editor': 'kaze'
            }
        self.res.append(var)

    def get_next_page(self):
        return self.html.select("#com_planning > div.navigation > a.next")

    def get_data(self):
        super(Kaze, self).get_data()
        if not self.timeline:
            self.stop_loop = True
