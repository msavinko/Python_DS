from datetime import datetime
from collections import Counter, defaultdict
from bs4 import BeautifulSoup
import requests
import re
import pytest

#-------------------------------#
#         Movies class          #
#-------------------------------#

class Movies:
	"""
	Analyzing data from movies.csv
	"""
	__csv_headers = ('movieId','title','genres')
	__csv_types = (int, str, str)

	"""
		инициализация класса с нужным путем и именем файла 
		https://ru.hexlet.io/courses/python-oop-basics/lessons/initialization/theory_unit#:~:text=%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%20__init__&text=%D0%AD%D1%82%D0%BE%D1%82%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%20%D0%BE%D1%82%D0%B2%D0%B5%D1%87%D0%B0%D0%B5%D1%82%20%D0%B7%D0%B0%20%D0%B8%D0%BD%D0%B8%D1%86%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8E,%D0%BA%D0%B0%D0%BA%20%D1%81%D0%B0%D0%BC%20%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%20%D0%B1%D1%8B%D0%BB%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD
	"""

	def __init__(self, path_to_the_file: str):
		self.filename = path_to_the_file      

	def __parse_line(cls, data_line: str): #парсим строку, убираем перенос строки
		data_line = data_line.replace('\n', '')

		if data_line.find('"') != -1: # убираем кавычки из названий фильмов, если они есть 
			splitted = re.split(r',\"|\",', data_line)
		else:
			splitted = data_line.split(',')

		return [cls.__csv_types[index](splitted[index]) 
		#cls - первый аргумент класса. Записывает все данные в соответствии с нужным хедером     
				for index in range(len(cls.__csv_headers))]

	def get_next_data_line(self):
		"""Read next data from file
		Yields:
			list with parsed values
		"""
		with open(self.filename, 'r', encoding='utf-8') as file:
			#opens filename in 'r' - reading mode and encoding it
			line = file.readline()              # header line, ignore
			line = file.readline()              # first data line
			while line:
				yield self.__parse_line(line)
				line = file.readline()          # data line
			#функция вернет генератор - итерируемый объект, который можно считать только один раз. Значение не хранится в памяти, а генерирует на лету  

	def __init__(self, path_to_the_file):
		self.filename = path_to_the_file
		self.__init_titles()
		
	def __init_titles(self):
		self.titles = {}
		for data in self.get_next_data_line():
			self.titles[data[0]] = data[1]
		# создаем отдельный список, где только названия фильмов

	def dist_by_release(self):
		"""
		The method returns a dict or an OrderedDict where the keys are years and the values are counts.
		You need to extract years from the titles. Sort it by counts descendingly.
		"""
		#dict - структура данных, хранит данные в формате ключ-значение. Доступ к значениям с помощью ключа. 
		#нужно посчитать сколько фильмов выпускалось каждый год
		years_distribution = Counter()
		#Класс Counter() модуля collections - это подкласс словаря dict для подсчета хеш-объектов
		
		for data in self.get_next_data_line():
			year = re.search(r'\((\d{4})\)', data[1]) #регулярка, которая ищет 4 цифры, идущие в скобках в дате и запиысывает в data[1]           
			if year:
				year = year.group(1)
			else:
				year = 'Null'
			years_distribution[year] += 1
		dictionary = dict(years_distribution.most_common())
		del dictionary['Null']
		return dictionary    

		#return dict(years_distribution.most_common())
		#Метод Counter.most_common() возвращает список из n наиболее распространенных элементов и их количество от наиболее распространенных до наименее. 
		#Элементы с равным количеством упорядочены в порядке, в котором они встречаются первыми.

	

	def dist_by_genres(self):
		"""
		The method returns a dict where the keys are genres and the values are counts.
		Sort it by counts descendingly.
		"""
		genres_distribution = Counter()

		for data in self.get_next_data_line():
			genres = data[2].split('|') #сплитит жанры 
			for genre in genres:
				genre = genre.strip() 
				#Возвращает копию указанной строки, с обоих концов которой устранены указанные символы.
				#Если не указана, будут устранены пробельные символы.
				if genre:
					genres_distribution[genre] += 1
		dictionary = dict(genres_distribution.most_common())
		del dictionary['(no genres listed)']
		return dictionary   
		#return dict(genres_distribution.most_common())

	def most_genres(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and
		the values are the number of genres of the movie. Sort it by numbers descendingly.
		"""
		dict_movies = {}
		for data in self.get_next_data_line():
			dict_movies[data[1]] = len(data[2].split('|'))

		return dict(sorted(dict_movies.items(), key=lambda x: x[1], reverse=True)[:n])
		#сортировка словаря по x[1] элементу кортежа в обратном порядке 

	def get_movie_title(self, movie_id):
		"""
		The method receives a list of IDs (as int) as input and returns a list of movie titles
		"""
		return self.titles.get(movie_id) #Возвращает значение из словаря по указанному ключу.
		"""
		Декоратор @lru_cache() модуля functools оборачивает функцию с переданными в нее аргументами 
		и запоминает возвращаемый результат соответствующий этим аргументам. Такое поведение может 
		сэкономить время и ресурсы, когда дорогая или связанная с вводом/выводом функция периодически
		 вызывается с одинаковыми аргументами.
		"""


#-------------------------------#
#       Statistics class        #
#-------------------------------#

class Statistics:
	"""
	Statistics utils
	"""
	def average(values: list):
		"""
		Get average value of values list
		"""
		return sum(values) / len(values)

	def median(values: list):
		"""
		Get median value of values list
		"""
		if len(values) == 0:
			raise ValueError('provided list is empty')

		if len(values) == 1:
			return float(values[0])

		values = sorted(values)
		mid = int(len(values) / 2)
		if len(values) % 2:
			return float(values[mid])
		return (values[mid - 1] + values[mid]) / 2.0

	def variance(values: list):  # разброс оценок (дисперсия)
		"""
		Calculate variance of values list
		"""
		if len(values) == 0:
			raise ValueError('provided list is empty')

		if len(values) == 1:
			return 0

		values = sorted(values)
		return values[len(values) - 1] - values[0]


#-------------------------------#
#        Ratings class          #
#-------------------------------#

class Ratings:
	"""
	Analyzing data from ratings.csv
	"""
	__csv_headers = ('userId','movieId','rating','timestamp')
	__csv_separator = ','
	__csv_types = (int, int, float, int)

	def __init__(self, path_to_the_file: str):
		self.filename = path_to_the_file

	def __parse_line(cls, data_line: str):
		splitted = data_line.split(cls.__csv_separator)
		return [cls.__csv_types[index](splitted[index]) 
				for index in range(len(cls.__csv_headers))]

	def get_next_data_line(self):
		"""
		Read next data from file
		Yields:
			list with parsed values
		"""
		with open(self.filename, 'r', encoding='utf-8') as file:
			line = file.readline()              # header line, ignore
			line = file.readline()              # first data line
			while line:
				yield self.__parse_line(line)
				line = file.readline()          # data line
	
	class Movies:
		"""
		Analyzing movies data from ratings.csv
		"""
		def __init__(self, ratings_cls, movies_cls: Movies):
			if not isinstance(ratings_cls, Ratings): # проверяем принадлежность экземпляра к классу
				raise ValueError('invalid Movies class object')
			if not isinstance(movies_cls, Movies): # проверяем принадлежность экземпляра к классу
				raise ValueError('invalid Movies class object')
			self.ratings = ratings_cls
			self.movies_cls = movies_cls

		def dist_by_year(self): # в каком году поставлена оценка (рейтинг)
			"""
			The method returns the years distribution by ratings count,
			sorted by years ascendingly.

			Returns:
				dict: a dict where the keys are years and the values are counts of ratings
			"""
			years_distribution = Counter() # количество оценок за каждый год

			for data in self.ratings.get_next_data_line():
				year = datetime.fromtimestamp(data[3]).year # извлекаем год из последнего столбца
				years_distribution[year] += 1

			return dict(sorted(years_distribution.items())) # от более ранних к более поздним


		def dist_by_rating(self): # количество оценок по каждому значению рейтинга (от 0.5 до 5.0)
			"""
			The method returns the ratings distribution by counts,
			sorted by ratings ascendingly.

			Returns:
				dict: a dict where the keys are ratings and the values are counts
			"""
			ratings_distribution = Counter()

			for data in self.ratings.get_next_data_line():
				ratings_distribution[data[2]] += 1

			return dict(sorted(ratings_distribution.items())) # от низких рейтингов к высоким

		def top_by_num_of_ratings(self, top_size: int): # фильмы с наибольшим количеством оценок
			"""
			The method returns top-n movies by the number of ratings,
			sorted by numbers descendingly.

			Returns:
				dict: a dict where the keys are movie titles and the values are numbers
			"""
			top_movies = Counter()

			for data in self.ratings.get_next_data_line():
				top_movies[self.movies_cls.get_movie_title(data[1])] += 1

			return dict(top_movies.most_common(top_size)) # наиболее часто встречающиеся элементы в порядке убывания встречаемости

		def top_by_ratings(self, n, metric=Statistics.average): # фильмы с наивысшими оценками (по средней)
			"""
			The method returns top-n movies by the `average` or `median` of the ratings,
			sorted by metric descendingly.
			
			Returns:
				dict: a dict where the keys are movie titles and the values are metric values
			"""
			all_movies = defaultdict(list)

			for data in self.ratings.get_next_data_line():
				all_movies[self.movies_cls.get_movie_title(data[1])].append(data[2])

			for movie in all_movies:
				all_movies[movie] = round(metric(all_movies[movie]), 2)

			return dict(sorted(all_movies.items(), key=lambda item: item[1], reverse=True)[:n])

		def top_controversial(self, n):  # фильмы с наивысшим разбросом оценок
			"""
			The method returns top-n movies by the variance of the ratings,
			sorted by variance descendingly.

			Returns:
				dict: a dict where the keys are movie titles and the values are the variances
			"""
			all_movies = defaultdict(list)

			for data in self.ratings.get_next_data_line():
				all_movies[self.movies_cls.get_movie_title(data[1])].append(data[2])

			for movie in all_movies:
				all_movies[movie] = round(Statistics.variance(all_movies[movie]), 2)

			return dict(sorted(all_movies.items(), key=lambda item: item[1], reverse=True)[:n])
		
	class Users(Movies):
		def dist_by_ratings_number(self): # распределение пользователей по количеству оценок
			"""
			The method returns the distribution of users by the number of ratings made by them,
			sorted by ratings ascendingly.

			Returns:
				dict: a dict where the keys are users and the values are number of ratings
			"""
			ratings_distribution = Counter()

			for data in self.ratings.get_next_data_line():
				ratings_distribution[data[0]] += 1

			return dict(sorted(ratings_distribution.items(), key=lambda item: item[1]))

		def dist_by_ratings_values(self, metric=Statistics.average): # распределение пользователей по величине оценок (по средней)
			"""
			The method returns the distribution of users by `average` or `median` ratings made by them,
			sorted by ratings ascendingly.

			Returns:
				dict: a dict where the keys are users and the values are metric of ratings
			"""
			all_ratings = defaultdict(list)

			for data in self.ratings.get_next_data_line():
				all_ratings[data[0]].append(data[2])

			for user in all_ratings:
				all_ratings[user] = round(metric(all_ratings[user]), 2)

			return dict(sorted(all_ratings.items(), key=lambda item: item[1]))

		def top_by_variance(self, n: int): # распределение пользователей по наивысшему разбросу оценок
			"""
			The method returns top-n users with the biggest variance of their ratings,
			sorted by variance descendingly.

			Returns:
				dict: a dict where the keys are users and the values are the variances
			"""
			all_ratings = defaultdict(list)

			for data in self.ratings.get_next_data_line():
				all_ratings[data[1]].append(data[2])

			for user in all_ratings:
				all_ratings[user] = round(Statistics.variance(all_ratings[user]), 2)

			return dict(sorted(all_ratings.items(), key=lambda item: item[1], reverse=True)[:n])


		
#-------------------------------#
#          Links class          #
#-------------------------------#

class Links:
	"""
	Analyzing data from links.csv
	"""
	__csv_headers = ('movieId','imdbId','tmdbId')
	__csv_separator = ','
	__csv_types = (int, str, lambda x: int(x) if x else 0)

	__film_page_base_urls = {
		'movielens': 'https://movielens.org/movies/',
		'imdb': 'https://www.imdb.com/title/tt',
		'tmdb': 'https://www.themoviedb.org/movie/'
	}

	def __init__(self, path_to_the_file: str, movies_cls: Movies):
		self.filename = path_to_the_file
		if not isinstance(movies_cls, Movies):
			"""
			Функция isinstance() вернет True, если проверяемый объект object является экземпляром указанного класса 
			или его подкласса.
			"""
			raise ValueError('invalid Movies class object')
		self.movies_cls = movies_cls
		#проверяем наличие фильма с таким айди в классе movies

	@classmethod
	def __parse_line(cls, data_line: str):
		splitted = data_line.replace('\n', '').split(cls.__csv_separator)
		return [cls.__csv_types[index](splitted[index]) 
				for index in range(len(cls.__csv_headers))]

	def get_next_data_line(self):
		"""Read next data from file
		Yields:
			list with parsed values
		"""
		with open(self.filename, 'r', encoding='utf-8') as file:
			line = file.readline()              # header line, ignore
			line = file.readline()              # first data line
			while line:
				yield self.__parse_line(line)
				line = file.readline()          # data line

	def __get_imdb_all_fields(self, movie_imdb_id: str):
		# request page
	  
		page = requests.get(self.__film_page_base_urls['imdb'] + movie_imdb_id)
		#requests.get(webpage) Этот метод используется для запроса содержимого URL-адреса с сервера
		if page.status_code != 200: 
		#The 200 OK status code means that the request was successful,
			raise RuntimeError("imdb request failed")

		# get info block
		soup = BeautifulSoup(page.text, features='html.parser')
		#print('FIRST SOUP')
		#print(soup)
		#print('---------------------------------')
		#Beautiful Soup — это библиотека Python для извлечения данных из файлов HTML и XML. 
		#Beautiful Soup превращает сложный HTML-документ в сложное дерево объектов Python.
		soup = soup.find_all('div', attrs={'class': 'ipc-page-content-container'})[5]
		#находим все с указанным тэгом и классом 
		#print('SECOND SOUP')
		#print(soup)
		#print('---------------------------------')
		soup = soup.find_all('li', attrs={'role': 'presentation', 'class': 'ipc-metadata-list__item'})
		#print('THIRD SOUP')
		#print(soup)
		#print('---------------------------------')

		# parse all avaliable info
		result = {}
		for data_line in soup:
			# get label and value
			row_name = data_line.find(attrs={'class': 'ipc-metadata-list-item__label'})
			if row_name is None:
				continue
			row_name = row_name.text.strip() # удаляет все начальные и конечные пробелы
			row_value = data_line.find(attrs={'class': 'ipc-metadata-list-item__content-container'})
			result[row_name] = row_value.text if row_value is not None else None
		#print('RESULT')
		#print(result)
		#print('---------------------------------')
		return result
	
	def __get_imdb_movie_info(self, movie_links, list_of_fields):
		all_fields = self.__get_imdb_all_fields(str(movie_links[1]))
		result = [all_fields.get(field) for field in list_of_fields]
		return [str(movie_links[0]), *result]

	def get_imdb(self, list_of_movies, list_of_fields):
		"""
		The method returns a list of lists [movieId, field1, field2, field3, ...] for the list of movies given as the argument (movieId).
		For example, [movieId, Director, Budget, Cumulative Worldwide Gross, Runtime].
		The values should be parsed from the IMDB webpages of the movies.
		Sort it by movieId descendingly.
		"""
		imdb_info = [self.__get_imdb_movie_info(data, list_of_fields) 
					 for data in self.get_next_data_line()
					 if data[0] in list_of_movies]
		print(imdb_info)
		return list(sorted(imdb_info, key=lambda fields: fields[0]))

	def top_directors(self, n):
		"""
		The method returns a dict with top-n directors where the keys are directors and 
		the values are numbers of movies created by them. Sort it by numbers descendingly.
		"""
		directors_list = [self.__get_imdb_movie_info(data, ['Director'])
						  for data in self.get_next_data_line()]
		directors_list = map(lambda pair: pair[1], directors_list)
		directors_counter = Counter(directors_list)
		return dict(directors_counter.most_common(n))

	def most_expensive(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and
		the values are their budgets. Sort it by budgets descendingly.
		"""
		budgets = [self.__get_imdb_movie_info(data, ['Budget'])
				   for data in self.get_next_data_line()]
		budgets = map(lambda item: (
						self.movies_cls.get_movie_title(self.__csv_types[0](item[0])),
						item[1] if item[1] is not None else ''
					), budgets)
		return dict(sorted(budgets, key=lambda item: item[1], reverse=True)[:n])

	def most_profitable(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and
		the values are the difference between worldwide gross and budget.
		Sort it by the difference descendingly.
		"""
		profits = []
		for data in self.get_next_data_line():
			info = self.__get_imdb_movie_info(data, ['Gross worldwide', 'Budget'])
			
			if info[1] is None or info[2] is None:
				profits.append([self.movies_cls.get_movie_title(data[0]), float('NaN')])
				continue
			
			values = (float(re.sub(r'[^\d.]', '', info[1])), float(re.sub(r'[^\d.]', '', info[2])))
			profits.append([
				self.movies_cls.get_movie_title(data[0]),
				round(values[0] - values[1], 2)])

		return dict(sorted(profits, key=lambda item: item[1] if item[1] is not None else '', reverse=True)[:n])

	def longest(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and
		the values are their runtime. If there are more than one version – choose any.
		Sort it by runtime descendingly.
		"""
		runtimes = [self.__get_imdb_movie_info(data, ['Runtime'])
					for data in self.get_next_data_line()]
		runtimes = map(lambda item: (
						self.movies_cls.get_movie_title(self.__csv_types[0](item[0])),
						item[1]
					), runtimes)
		
		def key_func(item):         # text to minutes
			if item[1] is None:
				return float('-inf')
			item = item[1].split()
			return int(item[0]) * 60 + int(item[2])
		
		return dict(sorted(runtimes, key=key_func, reverse=True)[:n])

	def top_cost_per_minute(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and
		the values are the budgets divided by their runtime. The budgets can be in different currencies – do not pay attention to it.
		The values should be rounded to 2 decimals. Sort it by the division descendingly.
		"""
		costs = []
		for data in self.get_next_data_line():
			info = self.__get_imdb_movie_info(data, ['Budget', 'Runtime'])
			
			if info[1] is None or info[2] is None:
				costs.append([self.movies_cls.get_movie_title(data[0]), float('NaN')])
				continue
			
			budget_value = float(re.sub(r'[^\d.]', '', info[1]))
			runtime_value = info[2].split()
			runtime_value = int(runtime_value[0]) * 60 + int(runtime_value[2])
			costs.append([
				self.movies_cls.get_movie_title(data[0]),
				round(budget_value / runtime_value, 2)])

		return dict(sorted(costs, key=lambda item: item[1] if item[1] is not None else '', reverse=True)[:n])


#-------------------------------#
#          Tags class           #
#-------------------------------#

class Tags:
	"""
	Analyzing data from tags.csv
	"""
	__csv_headers = ('userId', 'movieId', 'tag', 'timestamp')
	__csv_separator = ','
	__csv_types = (int, int, str, int)

	def __init__(self, path_to_the_file: str):
		self.filename = path_to_the_file

	def __parse_line(self, data_line: str):
		splitted = data_line.split(self.__csv_separator)
		return [self.__csv_types[index](splitted[index])
				for index in range(len(self.__csv_headers))]

	def get_next_data_line(self):
		"""Read next data from file
		Yields:
			list with parsed values
		"""
		with open(self.filename, 'r', encoding='utf-8') as file:
			line = file.readline()  # header line, ignore
			line = file.readline()  # first data line
			while line:
				yield self.__parse_line(line)
				line = file.readline()  # data line

	def most_words(self, n):
		"""
			The method returns top-n tags with most words inside,
			sorted by numbers descendingly.

			Returns:
				dict: a dict where the keys are tags
				and the values are the number of words inside the tag
		"""
		all_tags = {}

		for data in self.get_next_data_line():
			if data[2] not in all_tags:
				all_tags[data[2]] = len(re.findall(r'\b', data[2]))

		return dict(sorted(all_tags.items(), key=lambda item: item[1], reverse=True)[:n])

	def longest(self, n):
		"""
			The method returns top-n longest tags in terms of the number of characters,
			sorted by numbers descendingly.

			Returns:
				list: list of the longest tags
		"""
		all_tags = {}

		for data in self.get_next_data_line():
			if data[2] not in all_tags:
				all_tags[data[2]] = len(data[2])
		all_tags = dict(sorted(all_tags.items(), key=lambda item: item[1], reverse=True)[:n])

		return list(all_tags.keys())[:n]

	def most_words_and_longest(self, n):
		"""
		The method returns the intersection between top-n tags with most words inside and
		top-n longest tags in terms of the number of characters.
		Drop the duplicates. It is a list of the tags.
		"""
		big_tags = list(self.most_words(n).keys())
		long_tags = self.longest(n)
		for value in long_tags:
			if value not in big_tags:
				big_tags.append(value)

		return big_tags

	def most_popular(self, n):
		"""
		The method returns the most popular tags. 
		It is a dict where the keys are tags and the values are the counts.
		Drop the duplicates. Sort it by counts descendingly.
		"""
		all_tags = []

		for data in self.get_next_data_line():
			if data[2] not in all_tags:
				all_tags.append(data[2].lower())
		popular_tags = dict(Counter(all_tags).most_common(n))

		return popular_tags

	def tags_with(self, word):
		"""
		The method returns all unique tags that include the word given as the argument.
		Drop the duplicates. It is a list of the tags. Sort it by tag names alphabetically.
		"""
		tags_with_word = []

		for data in self.get_next_data_line():
			if word.lower() in data[2].lower():
				if data[2] not in tags_with_word:
					tags_with_word.append(data[2])

		return sorted(tags_with_word)
