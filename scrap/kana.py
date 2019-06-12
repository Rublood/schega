# -*- coding: utf-8 -*-
from datetime import datetime
import locale
from scrap.interface import InterfaceScrap

locale.setlocale(locale.LC_TIME, '')


class Kana(InterfaceScrap):

    def __init__(self, **kwargs):
        super(Kana, self).__init__(domain='https://www.kana.fr',
                                   url='https://www.kana.fr/wp-admin/admin-ajax.php?action=do_ajax&fn=ajax_get_planning&startDate=201905&nbMonth=3')

    def get_items(self):
        return self.html.select("div.item.support_manga")

    def add_item(self, item):
        var = {'name': str("%s - %s" % (item.find('h3').a.string, item.find('div', 'sub').string)).replace('\xa0', ' '),
               'date': datetime.strptime(item.find('div', 'date').string, '%d %B %Y').strftime("%d/%m/%Y"),
               'link': str(item.find('a').attrs['href']),
               'editor': 'kana'
               }
        if "Agenda" not in var['name']:
            self.res.append(var)
