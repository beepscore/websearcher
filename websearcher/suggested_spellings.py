#!/usr/bin/env python

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'websearcher')))

from websearcher import page_reader

# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':

    """
    Search words in input file. Use command line arguments.
    """

    python ./websearcher/suggested_spellings.py -search_terms "./websearcher_data/inputs/oovwords_fake.txt" -out_dir "./websearcher_data/results" -out_file "suggested_spelling_results.csv"

    reader = page_reader.PageReader("@./websearcher_data/inputs/page_reader_args.txt")
    actual = reader.suggested_spellings(["astma", "asthma", "bercitis"])
    expected = ["asthma", "", "bursitis"]
    self.assertEqual(expected, actual, '')
