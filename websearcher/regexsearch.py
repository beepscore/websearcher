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

    regex_dictionary = {}

    # python list comprehension
    for (misspelled_word, correct_word) in misspelled_words_list:
        # print(misspelled_word, correct_word)

        # {'aggravated': 'agrravated|agervated', }
        # if key in dict
        if correct_word in regex_dictionary:
            # append to value regex
            # {'aggravated': '(aggrabatd|aggravatred)'}
            regex_dictionary[correct_word] = regex_dictionary[correct_word] + "|" + misspelled_word

        else:
            # add key/value pair
            # {'aggravated': 'aggrabatd', 'aggressively': 'aggresivley' }
            regex_dictionary[correct_word] = misspelled_word

    print(regex_dictionary)


