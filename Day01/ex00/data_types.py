def data_types():
	my_int = 9
	my_str = 'I WANT A VACATION'
	my_float = 3.14
	my_bool = False
	my_list = ['wanna', 'go', 'to', 'NZ'] # список упорядоченный, изменяемый
	my_dict = {'country_of_dest':'New Zealand', 'city_of_dest':'Auckland'} # словарь упорядоченный, изменяемый
	my_tuple = tuple(['one', 2.88 , 5, 'six' ])  # кортеж упорядоченный, НЕизменяемый
	my_set = {'one', 'two', 'three'} # множество НЕупорядоченный, изменяемый. не может содержать повторения
	print(f'[{type(my_int).__name__}, {type(my_str).__name__}, {type(my_float).__name__},\
 {type(my_bool).__name__}, {type(my_list).__name__}, {type(my_dict).__name__},\
 {type(my_tuple).__name__}, {type(my_set).__name__}]')

if __name__ == '__main__':
	data_types()
