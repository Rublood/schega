# -*- coding: utf-8 -*-
from datetime import datetime

from scrap import *
from rss.pika import Pika
import click
import os
import io

package_dir = os.path.dirname(os.path.abspath(__file__))


def group_by(dict_list, key):
    tmp = dict()
    for item in dict_list:
        if not tmp.get(item[key]):
            tmp[item[key]] = []
        tmp[item[key]].append(item)
    return tmp


def filter_data(item_date, date):
    return datetime.strptime(date[0], '%d/%m/%Y') <= datetime.strptime(item_date, '%d/%m/%Y') <= datetime.strptime(
        date[1], '%d/%m/%Y')


def print_data(dict_list, reverse, date_param):
    grouped_by = group_by(dict_list, 'date')
    for date in sorted(grouped_by.items(), key=lambda x: datetime.strptime(x[0], '%d/%m/%Y'), reverse=reverse):
        if date_param == ("", "") or filter_data(date[0], date_param):
            for item in grouped_by[date[0]]:
                print("%s\n" % item)


def print_data_json(dict_list, reverse, date_param):
    data = "["
    grouped_by = group_by(dict_list, 'date')
    i = 0
    for date in sorted(grouped_by.items(), key=lambda x: datetime.strptime(x[0], '%d/%m/%Y'), reverse=reverse):
        i += 1
        j = 0
        if date_param == ("", "") or filter_data(date[0], date_param):
            for item in grouped_by[date[0]]:
                j += 1
                fin = '' if (len(grouped_by) == i and len(grouped_by[date[0]]) == j) else ',\n'
                data += '{"title":"' + item["name"] + '","start":"' + datetime.strptime(item["date"], '%d/%m/%Y').strftime('%Y-%m-%d') + '"}' + fin
    data += ']'
    return str(data)


default_editor_template = ["Glenat", "Kaze", "Kana", "Pika"]


@click.command()
@click.option('--editor', '-e', default=default_editor_template,
              help='Choose your editor can be multiple resources available(%s)' % default_editor_template,
              type=click.Choice(default_editor_template), multiple=True)
@click.option('--reverse', '-r', is_flag=True, default=True, help='reverse the date sort')
@click.option('--date', '-d', default=("", ""), help='select dates', type=str, nargs=2)
@click.argument('path', default="data.json", type=click.Path(exists=True))
def schega(editor, reverse, date, path):
    res = []
    default_editor = list(editor)
    for x in range(len(default_editor)):
        default_editor[x] = eval(default_editor[x])
    for x in default_editor:
        res.extend(x().res)
    print(res)

    if path:
        print(os.path.join(package_dir, path))
        with io.open(path, 'w', encoding='utf8') as f:
            f.write(print_data_json(res, reverse, date))
    else:
        print_data(res, reverse, date)


if __name__ == '__main__':
    schega()
