#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
# from ..websearcher import arg_reader
# put tests above websearcher directory
from websearcher import suggested_spellings_arg_reader


class TestSuggestedSpellingsArgReader(unittest.TestCase):

    def setUp(self):
        pass

    def test_args_default(self):
        reader = suggested_spellings_arg_reader.SuggestedSpellingsArgReader()
        args = reader.args(None)
        self.assertEqual("./websearcher_data/inputs", args.in_dir, '')
        self.assertEqual("oovwords.csv", args.in_file, '')
        self.assertEqual("./websearcher_data/results", args.out_dir, '')
        self.assertEqual("suggested_spellings_results.csv", args.out_file, '')

    def test_args_from_argument(self):
        reader = suggested_spellings_arg_reader.SuggestedSpellingsArgReader()

        in_dir = "../some_in_directory"
        in_file = "some_input.csv"
        out_dir = "../some_directory"
        out_file = "some_results.csv"

        test_commandline = ["-in_dir", in_dir, "-in_file", in_file, "-out_dir", out_dir, "-out_file", out_file]
        args = reader.args(test_commandline)

        self.assertEqual(in_dir, args.in_dir, '')
        self.assertEqual(in_file, args.in_file, '')
        self.assertEqual(out_dir, args.out_dir, '')
        self.assertEqual(out_file, args.out_file, '')

    def test_args_from_argument_file(self):
        reader = suggested_spellings_arg_reader.SuggestedSpellingsArgReader()
        # use fromfile_prefix_chars @ to read args from file
        args = reader.args(["@./websearcher_data/inputs/suggested_spellings_args.txt"])

        self.assertEqual("./websearcher_data/inputs", args.in_dir)
        self.assertEqual("oovwords.csv", args.in_file)
        self.assertEqual("./websearcher_data/results", args.out_dir)
        self.assertEqual("suggested_spellings_results.csv", args.out_file)

if __name__ == "__main__":
    unittest.main()
