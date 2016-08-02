#!/usr/bin/env python

from websearcher import top_hit

"""
Search words in input file. Use command line arguments.
"""

top_hit = top_hit.TopHit("@./websearcher_data/inputs/top_hit_args.txt")

actual = top_hit.top_hits_from_file()
print("results")
print('\n'.join(actual))
