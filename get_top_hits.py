#!/usr/bin/env python

from websearcher import top_hits

"""
Search words in input file. Use command line arguments.
"""

top_hits = top_hits.TopHits("@./websearcher_data/inputs/top_hit_args.txt")

actual = top_hits.top_hits_from_file()
print("results")
print('\n'.join(actual))
