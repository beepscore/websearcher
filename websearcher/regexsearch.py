#!/usr/bin/env python

import csv


# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':

    """
    Reads a csv file and creates regular expressions (regex).
    """
    misspelled_words = open('websearcher_data/inputs/regexwordstest.csv')

    misspelled_words_reader = csv.reader(misspelled_words)
    misspelled_words_list = list(misspelled_words_reader)
    print(misspelled_words_list)

    # http://stackoverflow.com/questions/1747817/create-a-dictionary-with-list-comprehension-in-python#1747827
    correct_words = {key: value for (key, value) in misspelled_words_list}

    print('******************')
    print(correct_words)
