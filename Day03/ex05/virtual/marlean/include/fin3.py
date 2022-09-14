#!/usr/bin/env python

from time import sleep
from bs4 import BeautifulSoup
import requests
import sys
import pytest

def check_args():
    if len(sys.argv) != 3:
        raise ValueError("No input")
    ar1 = sys.argv[1].lower()
    ar2 = sys.argv[2]
    return ar1, ar2

def connect_to_server(ar1):
    url = f'https://finance.yahoo.com/quote/{ar1}/financials?p={ar1}'
    page = requests.get(url, headers={'User-Agent': 'Custom'})
    if page.status_code != 200:
        raise ValueError("URL doesn't exist")
    return page

def test_connect_to_server_0():
    with pytest.raises(ValueError, match="URL doesn't exist"):
        connect_to_server('лол')

def test_connect_to_server_1():
    connect_to_server('lol') == requests.get('https://finance.yahoo.com/quote/lol/financials?p=lol', headers={'User-Agent': 'Custom'})

def page_parser(page, ar1, ar2):
    soup = BeautifulSoup(page.text, "html.parser")
    value = soup.find_all('div', class_ = 'D(tbr) fi-row Bgc($hoverBgColor):h')
    res = []
    for val in value:
        if (val.span.text == ar2):
            res.append(val.span.text)
            nums1 = val.find_all('div', class_ = 'Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)')
            nums2 = val.find_all('div', class_ = 'Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(tbc)')
            for num in nums1 + nums2:
                res.append(num.span.text)
    if not res:
        raise ValueError(f"Field {ar2} in {ar1} doesn't exist")
    return tuple(res)

def test_page_parser_0():
    assert page_parser(connect_to_server('MSFT'), 'MSFT', 'Total Revenue') == ('Total Revenue', '184,903,000', '143,015,000', '110,360,000', '168,088,000', '125,843,000')

def test_page_parser_1():
    assert page_parser(connect_to_server('aapl'), 'aapl', 'Total Revenue') == ('Total Revenue', '378,323,000', '274,515,000', '265,595,000', '365,817,000', '260,174,000')

def test_page_parser_2():
     with pytest.raises(ValueError):
         page_parser(connect_to_server('nokk'), 'nokk', 'Total Revenue')

def test_page_parser_tuple():
    assert type(page_parser(connect_to_server('MSFT'), 'MSFT', 'Total Revenue')) == type(tuple('5'))

def result():
    try:
        ar1, ar2 = check_args()
        page = connect_to_server(ar1)
        result = page_parser(page, ar1, ar2)
        print(result)
    except ValueError as exp:
        print('\033[91mException!', exp)

if __name__ == '__main__':
    result()

# py.test -s financial_test.py