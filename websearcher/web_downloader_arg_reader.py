#!/usr/bin/env python3

# References:
# https://docs.python.org/3/library/argparse.html
# http://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/argparse/index.html
# http://stackoverflow.com/questions/3853722/python-argparse-how-to-insert-newline-the-help-text

import argparse
from argparse import RawTextHelpFormatter


class WebDownloaderArgReader:
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
                                         $ ./web_downloader_arg_reader.py -h
                                         To specify an argument, prefix with -
                                         $ ./web_downloader_arg_reader.py -path a_path
                                         To read arguments from a file, prefix file name with @
                                         $ ./web_downloader_arg_reader.py @args.txt
                                         To specify arguments from command line and from a file
                                         $ ./web_downloader_arg_reader.py @args.txt -out_directory my_dir""",
                                         fromfile_prefix_chars='@',
                                         formatter_class=RawTextHelpFormatter,
                                         )

        parser.add_argument('-urls_file', action="store", dest="urls_file", default="../websearcher_inputs/urls.txt",
                            help='file with list of urls to download, one url per line. Defalult "../websearcher_inputs/urls.txt"')
        parser.add_argument('-out_directory', action="store", dest="out_directory", default="../websearcher_results",
                            help='name of output directory. Default "../websearcher_results"')

        if commandline is not None:
            args = parser.parse_args(commandline)
        else:
            args = parser.parse_args()

        return args
