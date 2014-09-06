#!/usr/bin/env python3

# References:
# http://docs.python.org/3.3/library/argparse.html?highlight=argparse#argparse
# http://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/argparse/index.html
# http://stackoverflow.com/questions/3853722/python-argparse-how-to-insert-newline-the-help-text

import argparse
from argparse import RawTextHelpFormatter


def main():
    '''
    Read arguments from command line or from a file.
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
    parser.add_argument('-uri_start', action="store", dest="uri_start",
                        help='''start of uri up to item number.
                        e.g. for url http://www.python-forum.org/viewforum.php?f=10&start=25
                        enter http://www.python-forum.org/viewforum.php?f=10&start='''
                        )
    parser.add_argument('-uri_end', action="store", dest="uri_end",
                        help='''end of uri after item number.
                        e.g. for url http://www.python-forum.org/viewforum.php?f=10&start=25
                        enter ""'''
                        )
    parser.add_argument('-item_start', action="store", dest="item_start",
                        help='''start item number.
                        e.g. for url http://www.python-forum.org/viewforum.php?f=10&start=25
                        enter 25
                        Default 1.'''
                        )
    parser.add_argument('-item_end', action="store", dest="item_end",
                        help='''end item number.
                        e.g. for url http://www.python-forum.org/viewforum.php?f=10&start=25
                        to search up to item 30 inclusive enter 30
                        Default 2.'''
                        )
    parser.add_argument('-outfile', action="store", dest="outfile",
                        help='name of output file. Default ./search_results.txt')

    arguments = parser.parse_args()
    print(arguments)
    print(arguments.expression)
    print(arguments.item_start)
    print(arguments.item_end)

if __name__ == "__main__":
    main()
