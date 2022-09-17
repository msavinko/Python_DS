import sys

def all_stock():

	my_args = sys.argv[1].replace(' ', '').split(',')
	for arg in my_args:
		if arg == '':
			
	print(my_args)

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
	# if arg.capitalize() in COMPANIES:
	# 	print(f'{arg} stock price is {STOCKS[COMPANIES[arg.capitalize]]}')




if __name__ == '__main__':
	if len(sys.argv) == 2:
		all_stock()

	# for arg in sys.argv:
	# 	all_stock(arg)

# take str as an arg

#.strip clean whitespaces and .split 