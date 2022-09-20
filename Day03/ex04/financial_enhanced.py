#!/usr/bin/env python3

from bs4 import BeautifulSoup
import sys
import httpx

def parse_info():
	#Принимаем адрес и заголовки. Заголовки используются для того, чтобы клиент и сервер понимали, как интерпретировать данные, отправляемые и получаемые в запросе и ответе.

	url = f'https://finance.yaho0.com/quote/{sys.argv[1]}/financials'
	headers={'User-Agent': 'Custom user agent'}
	try:
		website = httpx.get(url, headers=headers)
	except:
		print('\nWrong URL\n')
	if website.status_code != 200:
		raise Exception('Page is not found')
	# Создаем BeautifulSoup объект, который принимает Текст с веб страницы.
	# Используем встроенный в Питон парсер built-in HTML parser
	soup = BeautifulSoup(website.text, 'html.parser')
	# Находим элементы по HTML атрибутам на странице. берем целую строку fin-row
	elements = soup.find_all('div', attrs={'data-test' : 'fin-row'})
	for i in elements:
		if i.find('div', attrs={'title' : sys.argv[2]}) is not None:
			cols = i.find_all('div', attrs={'data-test' : 'fin-col'})
			my_list = [col.text for col in cols]
			return tuple([sys.argv[2], *my_list]) # звездочка убирает квадратные скобки
	raise Exception("Wrong statement name")

if __name__ == '__main__':
	if len(sys.argv) != 3:
		raise Exception('Wrong num of arg')

	try:
		print(parse_info())
	except:
		print('Invalid info')

#3 run this code
# python3 -m cProfile -s time financial_enhanced.py 'MSFT' 'Total Revenue' > profiling-http.txt

#4 run this code
# python3 -m cProfile -s ncalls financial_enhanced.py 'MSFT' 'Total Revenue' > profiling-ncalls.txt

#5 run this code
# python3 financial_enhanced.py 'MSFT' 'Total Revenue' > pstats-cumulative.txt

	# import cProfile
	# from pstats import Stats
	# from pstats import SortKey

	# pr = cProfile.Profile()
	# pr.enable()

	# parse_info()

	# pr.disable()
	# stats = Stats(pr)
	# stats.sort_stats(SortKey.CUMULATIVE).print_stats(5)