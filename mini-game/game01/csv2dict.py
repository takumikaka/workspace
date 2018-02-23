# -*- coding: utf-8 -*-

import csv

def row_csv2dict(csv_file):
    dict_club = {}
    with open(csv_file) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            dict_club[row[0]] = row[1]
    return dict_club
