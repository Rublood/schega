# -*- coding: utf-8 -*-
from scrap.interface import print_data
from scrap import *

editor = [Glenat, Kaze, Kana]
res = []
for x in editor:
    res.extend(x().res)
print_data(res)
