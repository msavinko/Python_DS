def dict_sorter():
	list_of_tuples = [
		('Russia', '25'),
		('France', '132'),
		('Germany', '132'),
		('Spain', '178'),
		('Italy', '162'),
		('Portugal', '17'),
		('Finland', '3'),
		('Hungary', '2'),
		('The Netherlands', '28'),
		('The USA', '610'),
		('The United Kingdom', '95'),
		('China', '83'),
		('Iran', '76'),
		('Turkey', '65'),
		('Belgium', '34'),
		('Canada', '28'),
		('Switzerland', '26'),
		('Brazil', '25'),
		('Austria', '14'),
		('Israel', '12')
	]

	#MAKE A DICT OUT OF TUPLE 
	#KEY - COUNTRY. VALUE - NUM
	dict_countries = dict((key,int(value)) for key, value in list_of_tuples)

	# DISPLAY COUNTRY NAME IN DESC ORDER BY NUM, ALPHA ORDER BY NAME IF NUM ARE EQUAL (its easier to sort a list and print it)
	sorted_values = sorted(dict_countries.items(), key=lambda item: (-int(item[1]), item[0]))

	for key in sorted_values:
		print(f'{key[0]}')

if __name__ == '__main__':
	dict_sorter()
