from os import link
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
    # tag_data = Tags('tags.csv')
    # print(tag_data.most_words(5))
    # print(tag_data.longest(5))
    # print(tag_data.most_words_and_longest(5))
    # print(tag_data.__rows)
    # print(tag_data.most_popular(50000000))
    # print(tag_data.tags_with('one'))
    # tag_data.Info.tags_with(tag_data)
    
    links_data = Links("links.csv")
    list_of_fields = ['directors', 'wins', 'productionBudget', 'lifetimeGross', 'runtime']
    movieIDs = links_data.get_list_of_links_field(0)
    test = links_data.get_imdb(movieIDs[15], list_of_fields)
    
    print(test)
    for i in test:
        print(i)
    return

if __name__ == "__main__":
    
    # try:
        if len(sys.argv) != 3:
            raise Exception("Wrong quantity of args!")
        main()
    # except Exception as err:
    #     print(err)