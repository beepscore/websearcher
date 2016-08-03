#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
from websearcher import suggested_spelling


class TestSpellingSuggester(unittest.TestCase):

    def setUp(self):
        pass

    # Apparently Python unittest runs tests in alphabetical order
    def test_suggested_spelling_pyethon(self):
        self.assertEqual("python", suggested_spelling.suggested_spelling("pyethon"), '')

    def test_suggested_spelling_python(self):
        self.assertEqual("", suggested_spelling.suggested_spelling("python"), '')

if __name__ == "__main__":
    unittest.main()
