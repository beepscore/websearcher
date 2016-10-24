#!/usr/bin/env python3

# use explicit relative import
# http://www.dabeaz.com/modulepackage/ModulePackage.pdf
from . import top_hit_arg_reader
from . import top_hit

import os
import csv


class TopHits:
    """
    Read input file, use browser to search for top hit, write result to output file
    """

    def __init__(self, argfile):
        """
        Initialize the class.

        :param argfile: file with arguments. Don't version control argfile. Put it outside project directory.
        :return: None
        """
        self.arg_reader = top_hit_arg_reader.TopHitArgReader()
        self.args = self.arg_reader.args([argfile])
        self.in_dir = self.args.in_dir
        self.in_file = self.args.in_file
        self.out_dir = self.args.out_dir
        self.out_file = self.args.out_file

    def top_hits_from_file_to_file(self):
        """
        Read input file
        uses browser to search for top hit
        writes to output file
        """
        in_file_full_path = os.path.join(self.in_dir, self.in_file)
        out_file_full_path = os.path.join(self.out_dir, self.out_file)

        # Use "with" to attempt to avoid ResourceWarning about unclosed file.
        # "with" automatically closes file at end of block, even if exception was raised
        # http://stackoverflow.com/questions/6159900/correct-way-to-write-line-to-file-in-python#6159912
        # https://www.python.org/dev/peps/pep-0343/
        # Unfortunately warning is still present. May be coming from somewhere else.

        with open(in_file_full_path, 'r') as input_file, open(out_file_full_path, 'w', newline='') as output_file:

            # use csv.writer to escape commas within result string
            # https://docs.python.org/3.5/library/csv.html
            # format excel style. Leaves inner quotes ".
            # csv_writer = csv.writer(output_file, dialect='excel')
            # format unix style. Leaves inner quotes ".
            csv_writer = csv.writer(output_file, dialect='unix')

            line_number = 1
            for line in input_file.readlines():
                print('input line number: ' + str(line_number) + ' line: ' + line)
                search_string = line.split(",")[0]

                count = ""
                if line is not None and len(line.split(",")) > 1:
                    count = line.split(",")[1]

                print("searching...")
                search_result = top_hit.top_hit(search_string)
                print("result: " + search_result)
                print()
                csv_writer.writerow([search_string, count, search_result])
                line_number += 1
