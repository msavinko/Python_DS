import sys

def func():
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

	if sys.argv[1].capitalize() not in COMPANIES:
		print('Unknown company')
		exit(1)
	for key, value in COMPANIES.items():
		if (sys.argv[1].capitalize() == key):
			my_key = value
	
	for key, value in STOCKS.items():
		if (my_key == key):
			print(value)

if __name__ == '__main__':
	if (len(sys.argv) == 2):
		func()
	else:
		exit(1)