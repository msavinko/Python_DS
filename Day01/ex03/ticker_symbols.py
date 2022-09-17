import sys

def stock(ticker):
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

	if ticker not in STOCKS:
		print('Unknown ticker')
		exit (1)

	invert_companies = {value: key for key, value in COMPANIES.items()} #invert dict. now keys are value and vice versa
	print (invert_companies[ticker], STOCKS[ticker])
		

if __name__ == '__main__':
	if (len(sys.argv) == 2):
		stock(sys.argv[1].upper())