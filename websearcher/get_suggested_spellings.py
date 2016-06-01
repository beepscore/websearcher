#!/usr/bin/env python

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'websearcher')))

from websearcher import page_reader

# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':

    """
    Search words in input file. Use command line arguments.
    """

    reader = page_reader.PageReader()
    # TODO
    #reader = page_reader.PageReader("@./websearcher_data/inputs/suggested_spelling_args.txt")
    actual = reader.suggested_spellings_from_file()
    expected = ["asthma", "", "bursitis"]
    self.assertEqual(expected, actual, '')
