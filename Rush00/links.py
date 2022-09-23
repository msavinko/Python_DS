import os
import json
from posixpath import split
import requests
from bs4 import BeautifulSoup
from collections import Counter

class Links:
	__rows = list()
	
	def __init__(self, path_to_the_file):
		self.path_to_the_file = path_to_the_file
		if not path_to_the_file.endswith('links.csv'):
			raise Exception("Wrong file. Need tags.csv")
		with open(path_to_the_file, mode='r') as fin:
			if os.access(path_to_the_file, os.R_OK):
				self.__rows = fin.readlines()
			else:
				raise Exception("Can't open file")
	
	def get_list_of_links_field(self, field_num: int):
		if field_num < 0 or field_num > 2:
			raise Exception("Field num can't be less then 0 or more then 2")
		field = [int(i.split(',')[field_num]) for i in self.__rows[1:]]
		return field
	
	def __get_fieldLinks_by_movie_id(self, movieID: int):
		if movieID <= 0:
			raise Exception(f'Field num cant be less then 0')
		field = [i.split(',') for i in self.__rows[1:]]
		for i in field:
			if str(movieID) == i[0]:
				return tuple([i[0], i[1], i[2].strip()])
	
	def get_imdb(self, list_of_movies, list_of_fields):
		"""
		The method returns a list of lists [movieId, field1, field2, field3, ...] for the list of movies given as the argument (movieId).
		For example, [movieId, Director, Budget, Cumulative Worldwide Gross, Runtime].
		The values should be parsed from the IMDB webpages of the movies.
		Sort it by movieId descendingly.
		"""
		
		movieID_list = list()
		fields = ['directors', 'wins', 'productionBudget', 'lifetimeGross', 'runtime']
		
		try:
			len(list_of_movies)
			for i in list_of_movies:
				movieID = self.__get_fieldLinks_by_movie_id(int(i))
				base_url = 'https://www.imdb.com/title/tt' + movieID[1] + '/'
				html = requests.get(base_url, headers={'User-Agent': 'Custom'})
				if html.status_code == 200:
					html_to_bs = html.text
					soup = BeautifulSoup(html_to_bs, 'lxml')
					pages = soup.find('script', attrs={'type': 'application/json'})
					pages_json = json.loads(pages.text)
					
					try:
						idb__director = (pages_json['props']['pageProps']['mainColumnData']['directors'])[0]['credits'][0]['name']['nameText']["text"]
					except:
						idb__director = 'None'
					try:
						idb_wins = pages_json['props']['pageProps']['mainColumnData']['wins']['total']
					except:
						idb_wins = '-1'
					try:
						idb_budget = pages_json['props']['pageProps']['mainColumnData']['productionBudget']['budget']['amount']
					except:
						idb_budget = '-1'
					try:
						idb_gross = pages_json['props']['pageProps']['mainColumnData']['lifetimeGross']['total']['amount']
					except:
						idb_gross = '-1'
					try:
						idb_runtime = pages_json['props']['pageProps']['mainColumnData']['runtime']['seconds']
					except:
						idb_runtime = '-1'
						
					tmp = []
					tmp.append(movieID[0])
					for i in list_of_fields:
						if i == fields[0]:
							tmp.append(idb__director)
						elif i == fields[1]:
							tmp.append(idb_wins)
						elif i == fields[2]:
							tmp.append(idb_budget)
						elif i == fields[3]:
							tmp.append(idb_gross)
						elif i == fields[4]:
							tmp.append(idb_runtime)
					movieID_list.append(tmp)
				else:
					continue
		except:
			movieID = self.__get_fieldLinks_by_movie_id(int(list_of_movies))
			base_url = 'https://www.imdb.com/title/tt' + movieID[1] + '/'  
			html = requests.get(base_url, headers={'User-Agent': 'Custom'})
			if html.status_code == 200:
				html_to_bs = html.text
				soup = BeautifulSoup(html_to_bs, 'lxml')
				pages = soup.find('script', attrs={'type': 'application/json'})
				pages_json = json.loads(pages.text)
			
				try:
						idb__director = (pages_json['props']['pageProps']['mainColumnData']['directors'])[0]['credits'][0]['name']['nameText']["text"]
				except:
					idb__director = 'None'
				try:
					idb_wins = pages_json['props']['pageProps']['mainColumnData']['wins']['total']
				except:
					idb_wins = '-1'
				try:
					idb_budget = pages_json['props']['pageProps']['mainColumnData']['productionBudget']['budget']['amount']
				except:
					idb_budget = '-1'
				try:
					idb_gross = pages_json['props']['pageProps']['mainColumnData']['lifetimeGross']['total']['amount']
				except:
					idb_gross = '-1'
				try:
					idb_runtime = pages_json['props']['pageProps']['mainColumnData']['runtime']['seconds']
				except:
					idb_runtime = '-1'
			
				tmp = []
				tmp.append(movieID[0])
				for i in list_of_fields:
					if i == fields[0]:
						tmp.append(idb__director)
					elif i == fields[1]:
						tmp.append(idb_wins)
					elif i == fields[2]:
						tmp.append(idb_budget)
					elif i == fields[3]:
						tmp.append(idb_gross)
					elif i == fields[4]:
						tmp.append(idb_runtime)
				movieID_list.append(tmp)

		return(movieID_list)
	
	def top_directors(self, n):
		"""
		The method returns a dict with top-n directors where the keys are directors and 
		the values are numbers of movies created by them. Sort it by numbers descendingly.
		"""
		
		if n <= 0:
			raise Exception("Wrong n in Links.top_directors()!")
		
		movieIDs = self.get_list_of_links_field(0)
		list_of_directors = [i[1] for i in self.get_imdb(movieIDs[56:156], ['directors'])]
		return dict(Counter(list_of_directors).most_common(n))
	
	def most_expensive(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and
		the values are their budgets. Sort it by budgets descendingly.
		"""
		
		if n <= 0:
			raise Exception("Wrong n in Links.most_expensive()!")
		
		with open('movies.csv', mode='r') as fin:
			if os.access('movies.csv', os.R_OK):
				rows = fin.readlines()
			else:
				raise Exception("Can't open file movies.csv")
		
		splited_rows = [i.split(',') for i in rows[1:]]
		movieIDs = self.get_list_of_links_field(0)
		list_of_budgets = [i for i in self.get_imdb(movieIDs[56:156], ['productionBudget'])]
		
		title_budget = []
		for i in list_of_budgets:
			for j in splited_rows:
				if i[0] == j[0]:
					title_budget.append([j[1], i[1]])
		
		return dict(sorted(title_budget, reverse=True, key=lambda el: el[1])[:n])
	
	def most_profitable(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and
		the values are the difference between cumulative worldwide gross and budget.
		Sort it by the difference descendingly.
		"""
		
		if n <= 0:
			raise Exception("Wrong n in Links.most_profitable()!")
		
		with open('movies.csv', mode='r') as fin:
			if os.access('movies.csv', os.R_OK):
				rows = fin.readlines()
			else:
				raise Exception("Can't open file movies.csv")
		
		splited_rows = [i.split(',') for i in rows[1:]]
		movieIDs = self.get_list_of_links_field(0)
		list_of_budgets = [i for i in self.get_imdb(movieIDs[56:156], ['productionBudget', 'lifetimeGross'])]
		
		title_budget = []
		for i in list_of_budgets:
			for j in splited_rows:
				if i[0] == j[0]:
					title_budget.append([j[1], int(i[2]) - int(i[1])])
		
		return dict(sorted(title_budget, reverse=True, key=lambda el: el[1])[:n])

	def longest(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and
		the values are their runtime. If there are more than one version â€“ choose any.
		Sort it by runtime descendingly.
		"""
		
		if n <= 0:
			raise Exception("Wrong n in Links.longest()!")
		
		with open('movies.csv', mode='r') as fin:
			if os.access('movies.csv', os.R_OK):
				rows = fin.readlines()
			else:
				raise Exception("Can't open file movies.csv")
		
		splited_rows = [i.split(',') for i in rows[1:]]
		movieIDs = self.get_list_of_links_field(0)
		list_of_budgets = [i for i in self.get_imdb(movieIDs[56:156], ['runtime'])]
		
		title_budget = []
		for i in list_of_budgets:
			for j in splited_rows:
				if i[0] == j[0]:
					title_budget.append([j[1], i[1]])
		
		return dict(sorted(title_budget, reverse=True, key=lambda el: el[1])[:n])
	
	def top_cost_per_minute(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and
		the values are the budgets divided by their runtime. The budgets can be in different currencies â€“ do not pay attention to it. 
		The values should be rounded to 2 decimals. Sort it by the division descendingly.
		"""
		
		if n <= 0:
			raise Exception("Wrong n in Links.most_profitable()!")
		
		with open('movies.csv', mode='r') as fin:
			if os.access('movies.csv', os.R_OK):
				rows = fin.readlines()
			else:
				raise Exception("Can't open file movies.csv")
		
		splited_rows = [i.split(',') for i in rows[1:]]
		movieIDs = self.get_list_of_links_field(0)
		list_of_budgets = [i for i in self.get_imdb(movieIDs[56:156], ['productionBudget', 'runtime'])]
		
		title_budget = []
		for i in list_of_budgets:
			for j in splited_rows:
				if i[0] == j[0]:
					title_budget.append([j[1], round(int(i[1]) / float(i[2]) ,2)])
		
		return dict(sorted(title_budget, reverse=True, key=lambda el: el[1])[:n])
	
	def top_winners(self, n):
		if n <= 0:
			raise Exception("Wrong n in Links.longest()!")
		
		with open('movies.csv', mode='r') as fin:
			if os.access('movies.csv', os.R_OK):
				rows = fin.readlines()
			else:
				raise Exception("Can't open file movies.csv")
		
		splited_rows = [i.split(',') for i in rows[1:]]
		movieIDs = self.get_list_of_links_field(0)
		list_of_budgets = [i for i in self.get_imdb(movieIDs[56:156], ['wins'])]
		
		title_budget = []
		for i in list_of_budgets:
			for j in splited_rows:
				if i[0] == j[0]:
					title_budget.append([j[1], i[1]])
		
		return dict(sorted(title_budget, reverse=True, key=lambda el: el[1])[:n])
	
	def top_ROC_in_prct(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and
		the values are the budgets divided by their runtime. The budgets can be in different currencies â€“ do not pay attention to it. 
		The values should be rounded to 2 decimals. Sort it by the division descendingly.
		"""
		
		if n <= 0:
			raise Exception("Wrong n in Links.most_profitable()!")
		
		with open('movies.csv', mode='r') as fin:
			if os.access('movies.csv', os.R_OK):
				rows = fin.readlines()
			else:
				raise Exception("Can't open file movies.csv")
		
		splited_rows = [i.split(',') for i in rows[1:]]
		movieIDs = self.get_list_of_links_field(0)
		list_of_budgets = [i for i in self.get_imdb(movieIDs[56:156], ['productionBudget', 'lifetimeGross'])]
		
		title_budget = []
		for i in list_of_budgets:
			for j in splited_rows:
				if i[0] == j[0]:
					title_budget.append([j[1], round(100 * (int(i[2]) - float(i[1])) / int(i[1]) ,2)])
		
		return dict(sorted(title_budget, reverse=True, key=lambda el: el[1])[:n])
	
	class Info:
		def get_imdb(self):
			print(f'The method returns a list of lists [movieId, field1, field2, field3, ...]' + 
				'for the list of movies given as the argument (movieId).' + 
				'For example, [movieId, Director, Budget, Cumulative Worldwide Gross, Runtime].' +
				'The values should be parsed from the IMDB webpages of the movies.' +
				'Sort it by movieId descendingly.' +
				' \n\n ' +
				'list of fields: directors, wins, productionBudget, lifetimeGross, runtime' +
				'\n' + 
				'Если значение порля -1 значит не удалось распарсить сайт\n' +
				'ROC - Return On Cost, (Gross - Budget) / Budget * 100%')
				
				