#!/usr/bin/env python

from websearcher import spelling_suggestions

"""
Search words in input file. Use command line arguments.
"""

suggester = spelling_suggestions.SpellingSuggester("@./websearcher_data/inputs/spelling_suggester_args.txt")
actual = suggester.suggested_spellings_from_file()
print("results")
print('\n'.join(actual))
