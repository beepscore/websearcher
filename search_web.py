#!/usr/bin/env python3

from websearcher import web_searcher_arg_reader
from websearcher import web_searcher

"""
Search for expression without instantiating an instance. Use command line arguments.
"""

# instantiate arg_reader
web_searcher_arg_reader = web_searcher_arg_reader.WebSearcherArgReader()
web_searcher_args = web_searcher_arg_reader.args()

expression = web_searcher_args.expression
search_directory = web_searcher_args.search_directory
out_dir = web_searcher_args.out_dir
out_file = web_searcher_args.out_file

print("Searching " + search_directory + " for expression " + expression)
print("Writing results to " + out_dir + " " + out_file)

web_searcher.WebSearcher.search_directory_write_results(expression,
                                                        search_directory,
                                                        out_dir,
                                                        out_file)

