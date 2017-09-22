#!/usr/bin/env python3

import csv
import os


class RegexSearch:
    """
    Reads a csv file and creates regular expressions (regex).
    """

    def __init__(self):
        """
        Initialize the class.
        """
        pass

    def write_regex(self):
        """
        Reads a csv file and creates regular expressions (regex).
        """
        misspelled_words = open('data/input/regexwordstest.csv')

        misspelled_words_reader = csv.reader(misspelled_words)
        misspelled_words_list = list(misspelled_words_reader)

        regex_dictionary = {}

        # python list comprehension
        for (misspelled_word, correct_word) in misspelled_words_list:
            # print(misspelled_word, correct_word)

            # {'aggravated': 'agrravated|agervated', }

            # use get() method, which returns None if not found, won't throw KeyError.
            # if dictionary doesn't contain key, regex_dictionary[correct_word] will throw KeyError.
            # To avoid error, either use get() or use conditional pre-check "if key in dictionary"
            regex = regex_dictionary.get(correct_word)

            if regex is not None:
                # append to value regex
                # {'aggravated': '(aggrabatd|aggravatred)'}

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
        filename = 'data/output/regex_output.csv'
        with open(filename, 'w') as csvfile:
            for key in regex_dictionary.keys():
                csvfile.write(key + ',' + regex_dictionary[key] + os.linesep)

#    def write_dict_to_csv(self, csv_file, dict_data):
#        try:
#            with open(csv_file, 'wb') as csvfile:
#                for key, value in dict_data:
#                    csvfile.write(key + ',' + value)
#        except IOError as (errno, strerror):
#            print("I/O error({0}): {1}".format(errno, strerror))
#            return
