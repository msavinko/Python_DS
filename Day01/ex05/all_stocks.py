import sys

def all_stock(elem):

	COMPANIES = {
	'Apple': 'AAPL',
	'Microsoft': 'MSFT',
	'Netflix': 'NFLX',
	'Tesla': 'TSLA',
	'Nokia': 'NOK'
	}
	STOCKS = {
	'AAPL': 287.73,
	'MSFT': 173.79,
	'NFLX': 416.90,
	'TSLA': 724.88,
	'NOK': 3.37
	}
	INVERT_COMPANIES = {value: key for key, value in COMPANIES.items()} 

	my_args = elem.replace(' ', '').split(',')
	for arg in my_args:
		if not arg:
			print('')
			exit(1)

	for arg in my_args:
		if arg.upper() in STOCKS:
			print(f'{arg.upper()} is a ticker symbol for {INVERT_COMPANIES[arg.upper()]}')
		elif arg.capitalize() in COMPANIES:
			print(f'{arg.capitalize()} stock price is {STOCKS[COMPANIES[arg.capitalize()]]}')
		else:
			print(f'{arg} is an unkonwn company of an unknown ticker symbol')

if __name__ == '__main__':
	if len(sys.argv) == 2:
		all_stock(sys.argv[1])
