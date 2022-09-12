#!/usr/bin/env python3

from bs4 import BeautifulSoup
import sys
import time
import requests

def parse_info():
	time.sleep(5)
	print('LETS PARSE')
	url = f'https://finance.yahoo.com/quote/{sys.argv[1]}/financials'
	website = requests.get(url, headers={'User-Agent' : 'Custom'}) #Принимаем адрес с параметрами
	


	# website = requests.get(f"https://finance.yahoo.com/quote/{sys.argv[1]}/financials", headers={'User-Agent' : 'Custom'})

	if website.status_code != 200:
		print('Page is not found')
		exit(1)
	print('Success')

	soup = BeautifulSoup(website.text, "html.parser")
	elements = soup.find_all('div', attrs={'data-test' : 'fin-row'})
	for i in elements:
		if i.find("div", attrs={'title' : sys.argv[2]}) is not None:
			cols = i.find_all('div', {'data-test' : 'fin-col'})
			return tuple([sys.argv[2], *[j.text for j in cols]])
	print("statement name is not found")
	exit(1)

# def main():
	




if __name__ == "__main__":
	if len(sys.argv) != 3:
		print('Wrong num of arg')
		exit(1)
	
	
	info = parse_info()
	if info is None:
		print('Invalid info')
		exit(1)
	print(info)