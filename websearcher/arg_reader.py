#!/usr/bin/env python3

# References:
# https://docs.python.org/3/library/argparse.html
# http://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/argparse/index.html
# http://stackoverflow.com/questions/3853722/python-argparse-how-to-insert-newline-the-help-text

import argparse
from argparse import RawTextHelpFormatter


class ArgReader():
    '''
    Read arguments from command line or from a file.
    '''

    def __init__(self):
        pass

    def args(self, commandline=None):
        '''
        Read arguments from method argument commandline, command line or a file.
        Reference http://stackoverflow.com/questions/18325211/argparse-fails-when-called-from-unittest-test
        '''

        parser = argparse.ArgumentParser(description='''    For help, use argument -h
                                         $ ./arg_reader.py -h
                                         To specify an argument, prefix with -
                                         $ ./arg_reader.py -expression an_expression -path a_path
                                         To read arguments from a file, prefix file name with @
                                         $ ./arg_reader.py @args.txt
                                         To specify arguments from command line and from a file
                                         $ ./arg_reader.py @args.txt -expression foo''',
                                         fromfile_prefix_chars='@',
                                         formatter_class=RawTextHelpFormatter,
                                         )

        parser.add_argument('-expression', action="store", dest="expression",
                            help='expression to search for, as a regular expression.'
                            )
        parser.add_argument('-url', action="store", dest="url",
                            help='''url to search
                            e.g. http://www.beepscore.com'''
                            )
        parser.add_argument('-out_directory', action="store", dest="out_directory", default="../websearcher_results",
                            help='name of output directory. Default "../websearcher_results"')
        parser.add_argument('-out_file', action="store", dest="out_file", default="results.txt",
                            help='name of output file. Default "results.txt"'
                            )

        if commandline is not None:
            args = parser.parse_args(commandline)
        else:
            args = parser.parse_args()

        return args
