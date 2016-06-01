#!/usr/bin/env python

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'websearcher')))

from websearcher import spelling_suggester

# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':

    """
    Search words in input file. Use command line arguments.
    """

    suggester = spelling_suggester.SpellingSuggester("@./websearcher_data/inputs/spelling_suggester_args.txt")
    actual = suggester.suggested_spellings_from_file()
    print("results")
    print('\n'.join(actual))
