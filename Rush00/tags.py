#!usr/bin/env python3

import os
import re
from collections import Counter

class Tags:
	__rows = list()
	
	def __init__(self, path_to_the_file) -> None:
		self.path_to_the_file = path_to_the_file
		if path_to_the_file != 'tags.csv':
			raise Exception("Wrong file. Need tags.csv")
		with open(path_to_the_file, mode='r') as fin:
			if os.access(path_to_the_file, os.R_OK):
				self.__rows = fin.readlines()
			else:
				raise Exception("Can't open file")
	
	def most_words(self, n):
		"""
		The method returns top-n tags with most words inside. It is a dict 
		where the keys are tags and the values are the number of words inside the tag.
		Drop the duplicates. Sort it by numbers descendingly.
		"""
		
		if n <= 0:
			raise Exception("Wrong n in Tags.most_words()!")
		uniq_tags = set([i.split(",")[2] for i in self.__rows[1:]])
		if n >= len(uniq_tags):
			n = len(uniq_tags)
		tags = dict.fromkeys(uniq_tags, 0)
		for i in tags.keys():
			tags[i] = len(i.split(' '))
		return dict(sorted(tags.items(), key=lambda item: item[1], reverse=True)[:n])
	
	def longest(self, n):
		"""
		The method returns top-n longest tags in terms of the number of characters.
		It is a list of the tags. Drop the duplicates. Sort it by numbers descendingly.
		"""
		
		if n <= 0:
			raise Exception("Wrong n in Tags.longest()!")
		uniq_tags = set([i.split(",")[2] for i in self.__rows[1:]])
		if n >= len(uniq_tags):
			n = len(uniq_tags)
		tags = dict.fromkeys(uniq_tags, 0)
		for i in tags.keys():
			tags[i] = len(i)
		big_tags = list()
		for i in range(n):
			big_tags.append(sorted(tags.items(), key=lambda item: item[1], reverse=True)[i][0])
		return big_tags
		
	def most_words_and_longest(self, n):
		"""
		The method returns the intersection between top-n tags with most words inside and 
		top-n longest tags in terms of the number of characters.
		Drop the duplicates. It is a list of the tags.
		"""

		if n <= 0:
			raise Exception("Wrong n in Tags.longest()!")
		most_words_list = list(self.most_words(n))
		longest_list = self.longest(n)
		return list(set(most_words_list) & set(longest_list))
	
	def most_popular(self, n):
		"""
		The method returns the most popular tags. 
		It is a dict where the keys are tags and the values are the counts.
		Drop the duplicates. Sort it by counts descendingly.
		"""
		
		if n <= 0:
			raise Exception("Wrong n in Tags.longest()!")
		return dict(Counter([i.split(",")[2] for i in self.__rows[1:]]).most_common(n))
	
	def tags_with(self, word: str):
		"""
		The method returns all unique tags that include the word given as the argument.
		Drop the duplicates. It is a list of the tags. Sort it by tag names alphabetically.
		"""
		
		uniq_tags = set([i.split(",")[2] for i in self.__rows[1:]])
		splited_uniq_tags = [re.split("\s|[:/']", i) for i in uniq_tags]
		
		for i in range(0, len(splited_uniq_tags)):
			for j in range(0, len(splited_uniq_tags[i])):
				splited_uniq_tags[i][j] = splited_uniq_tags[i][j].lower()
				for k in range(0, len(splited_uniq_tags[i][j])):
					if not splited_uniq_tags[i][j][k].isalnum():
						if splited_uniq_tags[i][j][k] != '-':
							splited_uniq_tags[i][j] = splited_uniq_tags[i][j].replace(splited_uniq_tags[i][j][k], ' ')
				splited_uniq_tags[i][j] = splited_uniq_tags[i][j].strip().replace(' ', '')

		big_tags_pre = []
		for i in splited_uniq_tags:
			if word.lower() in i:
				big_tags_pre.append(i)

		big_tags = []
		for i in big_tags_pre:
			tmp = ''
			for j in i:
				tmp += j + ' '
			big_tags.append(tmp)
	
		return sorted(big_tags)

	class Info:
		def tags_with(self):
			print(f'\n' +
					'######\n'
					'The method returns all unique tags that include the word given as the argument.' +
					'Drop the duplicates. It is a list of the tags. Sort it by tag names alphabetically.' + 
					'\n' +
					'\n' +
					'Может возвращать пустой лист, если искомого слова нет в тегах' +
					'\n######'
					'\n')
			