#!/usr/bin/env python3

from websearcher import spelling_suggester

"""
Search words in input file. Use command line arguments.
"""

suggester = spelling_suggester.SpellingSuggester("@./data/input/spelling_suggester_args.txt")
# suggested_spellings_from_file_to_file writes to file, doesn't return anything
suggester.suggested_spellings_from_file_to_file()
