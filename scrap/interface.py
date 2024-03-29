# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


class InterfaceScrap:
    def __init__(self, **kwargs):
        self.domain = kwargs.pop('domain', False)
        self.url = kwargs.pop('url', False)
        self.res = []
        self.html = kwargs.pop('html', False)
        self.nextpage = kwargs.pop('nextpage', False)
        self.timeline = kwargs.pop('timeline', False)
        self.stop_loop = kwargs.pop('stop_loop', False)
        super(InterfaceScrap, self).__init__(**kwargs)
        self.core()

    def core(self):
        while True and not self.stop_loop:
            self.get_data()
            for item in self.timeline:
                self.add_item(item)
            self.nextpage = self.get_next_page()
            if self.nextpage:
                self.nextpage = self.nextpage[0].attrs['href']
                self.url = self.domain + self.nextpage
            else:
                break
        # self.print_data()
        print(self.res)
        return self.res

    def get_data(self):
        data = requests.get(self.url)
        self.html = BeautifulSoup(data.text, 'html.parser')
        self.timeline = self.get_items()

    def get_items(self):
        raise Exception("not override")

    def add_item(self, item):
        raise Exception("not override")

    def get_next_page(self):
        return False
