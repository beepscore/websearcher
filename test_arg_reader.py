#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
# from ..websearcher import arg_reader
# put tests above websearcher directory
from websearcher import arg_reader


class TestArgReader(unittest.TestCase):

    def setUp(self):
        pass

    def test_args_default(self):
        reader = arg_reader.ArgReader()
        args = reader.args(None)
        self.assertEqual(None, args.expression, '')
        self.assertEqual(None, args.uri_start, '')
        self.assertEqual('', args.uri_end, '')
        self.assertEqual(1, args.item_start, '')
        self.assertEqual(2, args.item_end, '')
        self.assertEqual("../websearcher_results", args.out_directory, '')
        self.assertEqual("results.txt", args.out_file, '')

    def test_args_from_argument(self):
        reader = arg_reader.ArgReader()

        test_expression = "foo"
        test_uri_start = "bar"
        test_uri_end = "baz"
        test_item_start = "3"
        test_item_end = "7"
        test_out_directory = "../pages"
        test_out_file = "junk.txt"

        test_commandline = ["-expression", test_expression,
                            "-uri_start", test_uri_start,
                            "-uri_end", test_uri_end,
                            "-item_start", test_item_start,
                            "-item_end", test_item_end,
                            "-out_directory", test_out_directory,
                            "-out_file", test_out_file
                            ]
        args = reader.args(test_commandline)

        self.assertEqual(test_expression, args.expression, '')
        self.assertEqual(test_uri_start, args.uri_start, '')
        self.assertEqual(test_uri_end, args.uri_end, '')
        self.assertEqual(test_item_start, args.item_start, '')
        self.assertEqual(test_item_end, args.item_end, '')
        self.assertEqual(test_out_directory, args.out_directory, '')
        self.assertEqual(test_out_file, args.out_file, '')

    def test_args_from_argument_file(self):
        reader = arg_reader.ArgReader()

        args = reader.args(["@test_args.txt"])

        self.assertEqual("*raspberry", args.expression, '')
        self.assertEqual("http://www.python-forum.org/viewforum.php?f=10&start=",
                         args.uri_start, '')
        self.assertEqual("''", args.uri_end, '')
        self.assertEqual("25", args.item_start, '')
        self.assertEqual("27", args.item_end, '')
        self.assertEqual("../junk", args.out_directory, '')
        self.assertEqual("search_results.txt", args.out_file, '')

if __name__ == "__main__":
    unittest.main()
