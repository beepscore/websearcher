#!/usr/bin/env python3

from websearcher import top_hits

"""
Search words in input file. Use command line arguments.
"""

top_hits = top_hits.TopHits("@./data/input/top_hit_args.txt")

# top_hits_from_file_to_file writes to file, doesn't return anything
top_hits.top_hits_from_file_to_file()
