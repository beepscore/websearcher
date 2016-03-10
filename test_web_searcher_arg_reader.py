#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
# from ..websearcher import arg_reader
# put tests above websearcher directory
from websearcher import web_searcher_arg_reader


class TestWebSearcherArgReader(unittest.TestCase):

    def setUp(self):
        pass

    def test_args_default(self):
        reader = web_searcher_arg_reader.WebSearcherArgReader()
        args = reader.args(None)
        self.assertEqual(None, args.expression, '')
        self.assertEqual("../websearcher_data/downloads", args.search_directory, '')
        self.assertEqual("../websearcher_data/results/websearcher_results.txt", args.out_file, '')

    def test_args_from_argument(self):
        reader = web_searcher_arg_reader.WebSearcherArgReader()

        expression = "foo"
        search_directory = "some_search_directory"
        out_file = "../some_directory/some_results.txt"

        test_commandline = ["-expression", expression,
                            "-search_directory", search_directory,
                            "-out_file", out_file
                            ]
        args = reader.args(test_commandline)

        self.assertEqual(expression, args.expression, '')
        self.assertEqual(search_directory, args.search_directory, '')
        self.assertEqual(out_file, args.out_file, '')

    def test_args_from_argument_file(self):
        reader = web_searcher_arg_reader.WebSearcherArgReader()
        # use fromfile_prefix_chars @ to read args from file
        args = reader.args(["@./websearcher_data/inputs/web_searcher_args.txt"])

        self.assertEqual("app*", args.expression)
        self.assertEqual("./websearcher_data/downloads", args.search_directory)
        self.assertEqual("./websearcher_data/results/websearcher_results.txt",
                         args.out_file)

if __name__ == "__main__":
    unittest.main()
