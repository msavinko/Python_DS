# RUN THIS CODE TO ACTIVATE THE ENV
# python3 -m venv marlean_rush00 && source marlean_rush00/bin/activate && pip3 install jupyter && pip3 install pytest && /Users/marlean/Desktop/Python_DS/Rush00/marlean_rush00/bin/python3 -m pip install --upgrade pip

# RUN THE TESTS WIHT THIS COMMAND
# pytest movielens_analysis.py
from tags import *
from links import *
import sys

# def filename(name: str):
#     files = list(["tags.csv", "links.csv", "movies.csv", "ratings.csv"])
#     for i in sys.argv:
#         if i == name:
#             print(i)
#     # print(name)

def main():
	# filename("tags.csv")
	tag_data = Tags('tags.csv')
	# print(tag_data.most_words(5))
	# print(tag_data.longest(5))
	# print(tag_data.most_words_and_longest(5))
	# print(tag_data.__rows)
	# print(tag_data.most_popular(50000000))
	# print(tag_data.tags_with('one'))
	tag_data.Info.tags_with(tag_data)
	
	return

if __name__ == "__main__":
	
	try:
		if len(sys.argv) != 3:
			raise Exception("Wrong quantity of args!")
		main()
	except Exception as err:
		print(err)

#1.METHOD OF TAGS RETURN CORRECT DATA TYPE
def test_tags_dt_most_words():
	tag_data = Tags('tags.csv')
	test_teg = Tags.most_words(tag_data, 21)
	assert type(test_teg) is dict

def test_tags_dt_longest():
	tag_data = Tags('tags.csv')
	test_teg = Tags.longest(tag_data, 21)
	assert type(test_teg) is list

def test_tags_dt_most_words_and_longest():
	tag_data = Tags('tags.csv')
	test_teg = Tags.most_words_and_longest(tag_data, 21)
	assert type(test_teg) is list

def test_tags_dt_most_popular():
	tag_data = Tags('tags.csv')
	test_teg = Tags.most_popular(tag_data, 21)
	assert type(test_teg) is dict

def test_tags_dt_tags_with():
	tag_data = Tags('tags.csv')
	test_teg = Tags.tags_with(tag_data, 'travel')
	assert type(test_teg) is list

# 2.LISTS ELEMETS HAVE THE CORRECT DATA TYPES
