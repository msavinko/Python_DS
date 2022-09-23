# RUN THIS CODE TO ACTIVATE THE ENV
# python3 -m venv marlean_rush00 && source marlean_rush00/bin/activate && pip3 install jupyter && pip3 install pytest && /Users/marlean/Desktop/Python_DS/Rush00/marlean_rush00/bin/python3 -m pip install --upgrade pip && pip3 install requests

# RUN THE TESTS WIHT THIS COMMAND
# pytest movielens_analysis.py

from tags import *
from links import *
from movielens_analysis_new import *

class Test:

	# path = '/Users/marlean/goinfre/ml-latest-small/'
	path = ''
	check_num = 21
	tag_data = Tags(path + 'tags.csv')
	# link_data = Links(path + 'links.csv')
	mov_data = Movies(path + 'movies.csv')
	rating_data = Ratings(path + 'ratings.csv')
	mov_data = Movies(path + 'movies.csv')
	rating_mov_data = Ratings.Movies(rating_data, mov_data)

#1.METHOD OF TAGS RETURN CORRECT DATA TYPE
	#1.1.TAGS
	def test_tags_dt_most_words(self):
		result = Tags.most_words(self.tag_data, self.check_num)
		assert type(result) is dict

	def test_tags_dt_longest(self):
		result = Tags.longest(self.tag_data, self.check_num)
		assert type(result) is list

	def test_tags_dt_most_words_and_longest(self):
		result = Tags.most_words_and_longest(self.tag_data, self.check_num)
		assert type(result) is list

	def test_tags_dt_most_popular(self):
		result = Tags.most_popular(self.tag_data, self.check_num)
		assert type(result) is dict

	def test_tags_dt_tags_with(self):
		result = Tags.tags_with(self.tag_data, 'travel')
		assert type(result) is list
	
	#1.2.MOVIES
	def test_mov_dt_dist_by_release(self):
		result = Movies.dist_by_release(self.mov_data)
		assert type(result) is dict

	def test_mov_dt_dist_by_genres(self):
		result = Movies.dist_by_genres(self.mov_data)
		assert type(result) is dict

	def test_mov_dt_most_genres(self):
		result = Movies.most_genres(self.mov_data, self.check_num)
		assert type(result) is dict

	#1.3.RATINGS
	def test_rati_dt_dist_by_year(self):
		resutl = Ratings.Movies.dist_by_year(self.rating_mov_data)
		assert type(resutl) is dict

	def test_rati_dt_dist_by_rating(self):
		resutl = Ratings.Movies.dist_by_rating(self.rating_mov_data)
		assert type(resutl) is dict

	# def test_rati_dt_top_by_num_of_ratings(self):
	# 	resutl = Ratings.Movies.top_by_num_of_ratings(self.rating_mov_data, self.check_num)
	# 	assert type(resutl) is dict

	# def test_rati_dt_top_by_ratings(self):
	# 	resutl = Ratings.Movies.top_by_ratings(self.rating_mov_data)
	# 	assert type(resutl) is dict

	# def test_rati_dt_dist_by_year(self):
	# 	resutl = Ratings.Movies.dist_by_year(self.rating_mov_data)
	# 	assert type(resutl) is dict

	# def test_rati_dt_dist_by_year(self):
	# 	resutl = Ratings.Movies.dist_by_year(self.rating_mov_data)
	# 	assert type(resutl) is dict


# 2.LISTS ELEMETS HAVE THE CORRECT DATA TYPES

	def test_el_longest(self):
		result = Tags.longest(self.tag_data, self.check_num)
		assert (isinstance(result, list) and
			(set(map(type, result)) == {str})) # проверка что каждый эл-т возвращает верный тип данных
	
	def test_el_most_words_and_longest(self):
		result = Tags.most_words_and_longest(self.tag_data, self.check_num)
		assert (isinstance(result, list) and
			(set(map(type, result)) == {str})) # проверка что каждый эл-т возвращает верный тип данных
	
	def test_el_tags_with(self):
		result = Tags.tags_with(self.tag_data, 'travel')
		assert (isinstance(result, list) and
			(set(map(type, result)) == {str})) # проверка что каждый эл-т возвращает верный тип данных

# 3. SORTED

	# 3.1. TAG
	#sorted dictionary descending
	def test_sort_tag_most_words(self):
		result = Tags.most_words(self.tag_data, self.check_num)
		sorted_dict = True
		words = list(result.values())
		for i in range(1, len(words)):
			if words[i - 1] < words[i]: 
				sorted_dict = False
				break
		assert sorted_dict

	#sorted list
	def test_sort_tag_longest(self):
		result = Tags.longest(self.tag_data, self.check_num)
		sorted_list = True
		for i in range(1, len(result)):
			if len(result[i - 1]) < len(result[i]):
				sorted_list = False
				break
		assert sorted_list

	#sorted dictionary descending
	def test_sort_tag_most_popular(self):
		result = Tags.most_popular(self.tag_data, self.check_num)
		sorted_dict = True
		words = list(result.values())
		for i in range(1, len(words)):
			if words[i - 1] < words[i]: 
				sorted_dict = False
				break
		assert sorted_dict

	#sorted list
	def test_sort_tag_tags_with(self):
		result = Tags.tags_with(self.tag_data, 'travel')
		sorted_list = True
		for i in range(1, len(result)):
			if len(result[i - 1]) < len(result[i]):
				sorted_list = False
				break
		assert sorted_list
	
	# 3.2. MOVIES
	def test_sort_mov_dist_by_release(self):
		result = Movies.dist_by_release(self.mov_data)
		sorted_dict = True
		words = list(result.values())
		for i in range(1, len(words)):
			if words[i - 1] < words[i]: 
				sorted_dict = False
				break
		assert sorted_dict
		
	def test_sort_mov_dist_by_genres(self):
		result = Movies.dist_by_genres(self.mov_data)
		sorted_dict = True
		words = list(result.values())
		for i in range(1, len(words)):
			if words[i - 1] < words[i]: 
				sorted_dict = False
				break
		assert sorted_dict

	def test_sort_mov_most_genres(self):
		result = Movies.most_genres(self.mov_data, self.check_num)
		sorted_dict = True
		words = list(result.values())
		for i in range(1, len(words)):
			if words[i - 1] < words[i]: 
				sorted_dict = False
				break
		assert sorted_dict
