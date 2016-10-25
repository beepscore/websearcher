#!/usr/bin/env python3

from . import spelling_suggester_arg_reader
from . import suggested_spelling
import os


class SpellingSuggester:
    """
    Use browser to search for strings and return suggested spellings
    """

    def __init__(self, argfile):
        """
        Initialize the class.

        :param argfile: file with arguments. Don't version control argfile. Put it outside project directory.
        :return: None
        """
        self.arg_reader = spelling_suggester_arg_reader.SpellingSuggesterArgReader()
        self.args = self.arg_reader.args([argfile])
        self.in_dir = self.args.in_dir
        self.in_file = self.args.in_file
        self.out_dir = self.args.out_dir
        self.out_file = self.args.out_file

    def suggested_spellings(self, search_strings):
        """
        Use browser to search for strings
        returns suggested spellings
        returns empty string if browser doesn't suggest a spelling
        """
        results = []
        for search_string in search_strings:
            results.append(suggested_spelling.suggested_spelling(search_string))
        return results

    def suggested_spellings_from_file_to_file(self):
        """
        reads search_strings from in_file
        uses browser to search
        writes suggested_spellings to out_file
        """
        in_file_full_path = os.path.join(self.in_dir, self.in_file)
        out_file_full_path = os.path.join(self.out_dir, self.out_file)

        # Use "with" to attempt to avoid ResourceWarning about unclosed file.
        # "with" automatically closes file at end of block, even if exception was raised
        # http://stackoverflow.com/questions/6159900/correct-way-to-write-line-to-file-in-python#6159912
        # https://www.python.org/dev/peps/pep-0343/
        # Unfortunately warning is still present. May be coming from somewhere else.

        with open(in_file_full_path, 'r') as input_file, open(out_file_full_path, 'w') as output_file:
            line_number = 1
            for line in input_file.readlines():

                if line is None or line == "" or line == '\n':
                    # go to next iteration
                    line_number += 1
                    continue

                print()
                message = 'input line {0} {1}'.format(line_number, line).rstrip()
                print(message)
                search_string = line.split(",")[0]

                count = ""
                if len(line.split(",")) > 1:
                    count = line.split(",")[1]

                print("searching " + search_string)
                search_result = suggested_spelling.suggested_spelling(search_string)
                search_result_line = search_string + "," + count + "," + search_result
                print("output line " + search_result_line)
                output_file.write(search_result_line + '\n')
                line_number += 1
