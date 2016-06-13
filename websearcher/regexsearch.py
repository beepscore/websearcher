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
        # key is correct_word
        if correct_word in regex_dictionary:
            # append to value regex
            # {'aggravated': '(aggrabatd|aggravatred)'}

            regex = regex_dictionary[correct_word]

            first_letter_of_regex = regex[0]
            last_letter_of_regex = regex[-1]

            if first_letter_of_regex == '(':
                # remove first letter
                regex = regex[1:]

            if last_letter_of_regex  == ')':
                # remove last letter
                regex = regex[:-1]

            regex_dictionary[correct_word] = '(' + regex + "|" + misspelled_word + ')'

        else:
            # add key/value pair
            # {'aggravated': 'aggrabatd', 'aggressively': 'aggresivley' }
            regex_dictionary[correct_word] = misspelled_word

    print(regex_dictionary)


