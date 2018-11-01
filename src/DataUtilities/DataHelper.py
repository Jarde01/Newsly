import os

import pandas

def read_csv(path_to_csv: str=''):
    df = pandas.read_csv(path_to_csv, encoding='latin1')
    return df

def read_excel(path_to_excel: str):
    df = pandas.read_excel(open(path_to_excel, 'rb'))
    return df