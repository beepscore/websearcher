#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
from websearcher import spelling_suggester


class TestSpellingSuggester(unittest.TestCase):

    def setUp(self):
        pass

    def test_suggested_spellings(self):
        suggester = spelling_suggester.SpellingSuggester("@./data/input/spelling_suggester_args.txt")
        actual = suggester.suggested_spellings(["pythan", "python", "javascwipt", "swoft"])
        expected = ["python", "", "javascript", "swift"]
        self.assertEqual(expected, actual, '')


if __name__ == "__main__":
    unittest.main()
