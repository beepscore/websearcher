#!/usr/bin/env python3

# References:
# https://docs.python.org/3/library/argparse.html
# http://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/argparse/index.html
# http://stackoverflow.com/questions/3853722/python-argparse-how-to-insert-newline-the-help-text

import argparse
from argparse import RawTextHelpFormatter


class WebSearcherArgReader:
    """
    Read arguments from command line or from a file.
    """

    def __init__(self):
        pass

    def args(self, commandline=None):
        """
        Read arguments from method argument commandline, command line or a file.
        Reference http://stackoverflow.com/questions/18325211/argparse-fails-when-called-from-unittest-test
        """

        parser = argparse.ArgumentParser(description="""    For help, use argument -h
                                         $ ./web_searcher_arg_reader.py -h
                                         To specify an argument, prefix with -
                                         $ ./web_searcher_arg_reader.py -expression an_expression
                                         To read arguments from a file, prefix file name with @
                                         $ ./web_searcher_arg_reader.py @args.txt
                                         To specify arguments from command line and from a file
                                         $ ./web_searcher_arg_reader.py @args.txt -expression foo""",
                                         fromfile_prefix_chars='@',
                                         formatter_class=RawTextHelpFormatter,
                                         )

        parser.add_argument('-expression', action="store", dest="expression", default="foo",
                            help='expression to search for, as a regular expression.')
        parser.add_argument('-search_directory', action="store", dest="search_directory", default="./websearcher_data/downloads",
                            help='directory to search. Default "./websearcher_data/downloads"')
        parser.add_argument('-out_dir', action="store", dest="out_dir", default="./websearcher_data/results",
                            help='name of output directory. Default "./websearcher_data/results"')
        parser.add_argument('-out_file', action="store", dest="out_file", default="websearcher_results.txt",
                            help='name of output file. Default "websearcher_results.txt"')

        if commandline is not None:
            args = parser.parse_args(commandline)
        else:
            args = parser.parse_args()

        return args
