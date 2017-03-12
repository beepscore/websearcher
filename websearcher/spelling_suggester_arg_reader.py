#!/usr/bin/env python3

# References:
# https://docs.python.org/3/library/argparse.html
# http://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/argparse/index.html
# http://stackoverflow.com/questions/3853722/python-argparse-how-to-insert-newline-the-help-text

import argparse
from argparse import RawTextHelpFormatter


class SpellingSuggesterArgReader:
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
                                         $ ./page_reader_arg_reader.py -h
                                         To specify an argument, prefix with -
                                         $ ./page_reader_arg_reader.py -expression an_expression
                                         To read arguments from a file, prefix file name with @
                                         $ ./page_reader_arg_reader.py @args.txt
                                         To specify arguments from command line and from a file
                                         $ ./page_reader_arg_reader.py @args.txt -in_file foo.csv""",
                                         fromfile_prefix_chars='@',
                                         formatter_class=RawTextHelpFormatter,
                                         )

        parser.add_argument('-in_dir', action="store", dest="in_dir", default="./data/input",
                            help='name of input directory. Default "./data/input"')
        parser.add_argument('-in_file', action="store", dest="in_file", default="oovwords.csv",
                            help='input file of search words. Default "oovwords.csv"')
        parser.add_argument('-out_dir', action="store", dest="out_dir", default="./data/output",
                            help='name of output directory. Default "./data/output"')
        parser.add_argument('-out_file', action="store", dest="out_file", default="suggested_spellings_output.csv",
                            help='name of output file. Default "suggested_spellings_output.csv"')

        if commandline is not None:
            args = parser.parse_args(commandline)
        else:
            args = parser.parse_args()

        return args
