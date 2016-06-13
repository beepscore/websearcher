#!/usr/bin/env python

# http://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'websearcher')))

from websearcher import regex_search

# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':

    """
    Concatenate regex
    """

    regex_search = regex_search.RegexSearch()
    regex_search.write_regex()

