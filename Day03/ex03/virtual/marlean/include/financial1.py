#!/usr/bin/env python3

from bs4 import BeautifulSoup
import sys
import requests
import time

# def parse_html_yahoo():
#     time.sleep(5)
#     html_yahoo = requests.get(f"https://finance.yahoo.com/quote/{sys.argv[1]}/financials", headers={'User-Agent' : 'Custom'})
#     if html_yahoo.status_code != 200:
#         print("page is not found")
#         exit(1)
#     soup = BeautifulSoup(html_yahoo.text, "html.parser")
#     rows = soup.find_all('div', attrs={'data-test' : 'fin-row'})
#     for i in rows:
#         if i.find("div", attrs={'title' : sys.argv[2]}) is not None:
#             cols = i.find_all('div', {'data-test' : 'fin-col'})
#             return tuple([sys.argv[2], *[j.text for j in cols]])
#     print("statement name is not found")
#     exit(1)

def main():
    if len(sys.argv) != 3:
        print('Wrong number of arg')
        exit(1)

    time.sleep(5)
    url = 'https://finance.yahoo.com/quote/{sys.argv[1]}/financials'
    res = requests.get(url, headers={'User-Agent' : 'Custom'})
    if res != 200
        print('Page is not found')
    else:
        print(res)


if __name__ == "__main__":
    main()


    # fin_info = parse_html_yahoo()
    # if fin_info is None:
    #     print("Invalid info")
    #     exit(1)
    # print(fin_info)