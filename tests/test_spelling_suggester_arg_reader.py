#!/usr/bin/env python3

import unittest

import sys

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
# from ..websearcher import arg_reader
# put tests above websearcher directory
from websearcher import spelling_suggester_arg_reader


class TestSpellingSuggesterArgReader(unittest.TestCase):

    def setUp(self):
        pass

    def test_args_default(self):
        reader = spelling_suggester_arg_reader.SpellingSuggesterArgReader()
        print(reader)
        args = reader.args(None)
        self.assertEqual("./data/input", args.in_dir, '')
        self.assertEqual("input_words.csv", args.in_file, '')
        self.assertEqual("./data/output", args.out_dir, '')
        self.assertEqual("suggested_spellings_output.csv", args.out_file, '')

    def test_args_from_argument(self):
        reader = spelling_suggester_arg_reader.SpellingSuggesterArgReader()

        in_dir = "../some_in_directory"
        in_file = "some_input.csv"
        out_dir = "../some_directory"
        out_file = "some_output.csv"

        test_commandline = ["-in_dir", in_dir, "-in_file", in_file, "-out_dir", out_dir, "-out_file", out_file]
        args = reader.args(test_commandline)

        self.assertEqual(in_dir, args.in_dir, '')
        self.assertEqual(in_file, args.in_file, '')
        self.assertEqual(out_dir, args.out_dir, '')
        self.assertEqual(out_file, args.out_file, '')

    def test_args_from_argument_file(self):
        reader = spelling_suggester_arg_reader.SpellingSuggesterArgReader()
        # use fromfile_prefix_chars @ to read args from file
        # https://stackoverflow.com/questions/25084993/why-isnt-fromfile-prefix-chars-in-python-argparse-working/25084994#25084994
        # https://stackoverflow.com/questions/48650616/best-way-to-pass-command-line-arguments-via-file-in-python?noredirect=1&lq=1
        # https://micha-feigin.medium.com/on-using-config-files-with-pythons-argparse-8af09d0bdfb9
        # args = reader.args(["@./data/input/spelling_suggester_args.txt"])
        args = reader.args(["@./data/test_data/spelling_suggester_args.txt"])

        self.assertEqual("./data/input", args.in_dir)
        self.assertEqual("foo.csv", args.in_file)
        self.assertEqual("./data/output", args.out_dir)
        self.assertEqual("suggested_spellings_output.csv", args.out_file)


if __name__ == "__main__":
    unittest.main()
