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
        self.assertEqual(None, args.url, '')
        self.assertEqual("../websearcher_results/results.txt", args.out_file, '')

    def test_args_from_argument(self):
        reader = web_searcher_arg_reader.WebSearcherArgReader()

        test_expression = "foo"
        test_url = "bar"
        out_file = "../websearcher_results/websearcher_results.txt"

        test_commandline = ["-expression", test_expression,
                            "-url", test_url,
                            "-out_file", out_file
                            ]
        args = reader.args(test_commandline)

        self.assertEqual(test_expression, args.expression, '')
        self.assertEqual(test_url, args.url, '')
        self.assertEqual(out_file, args.out_file, '')

    def test_args_from_argument_file(self):
        reader = web_searcher_arg_reader.WebSearcherArgReader()
        # use fromfile_prefix_chars @ to read args from file
        args = reader.args(["@./test_args/web_searcher_args.txt"])

        out_file = "../websearcher_results/websearcher_results.txt"
        self.assertEqual("app*", args.expression)
        self.assertEqual("http://www.beepscore.com", args.url)
        self.assertEqual(out_file, args.out_file)

if __name__ == "__main__":
    unittest.main()
